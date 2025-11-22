from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional
import bleach
from ..models.feedback import Feedback
from ..schemas.feedback import FeedbackCreateRequest, FeedbackResponse, FeedbackPageResponse


class FeedbackService:
    """Service class for feedback business logic"""

    ANONYMOUS_USER = "익명"

    @staticmethod
    def sanitize_string(input_str: Optional[str]) -> Optional[str]:
        """
        Sanitize string to prevent XSS attacks
        
        Args:
            input_str: Input string to sanitize
            
        Returns:
            Sanitized string
        """
        if input_str is None:
            return None
        # Use bleach to clean HTML and prevent XSS
        return bleach.clean(input_str, tags=[], strip=True)

    @classmethod
    def create_feedback(cls, request: FeedbackCreateRequest, db: Session) -> FeedbackResponse:
        """
        Create a new feedback with XSS protection
        
        Args:
            request: Feedback creation request
            db: Database session
            
        Returns:
            Created feedback response
        """
        # Sanitize inputs for XSS protection
        sanitized_username = cls.sanitize_string(request.username)
        sanitized_message = cls.sanitize_string(request.message)

        # Set anonymous username if empty
        if not sanitized_username or sanitized_username.strip() == "":
            sanitized_username = cls.ANONYMOUS_USER

        # Create feedback entity
        feedback = Feedback(
            username=sanitized_username,
            message=sanitized_message
        )

        # Save to database
        db.add(feedback)
        db.commit()
        db.refresh(feedback)

        return FeedbackResponse.model_validate(feedback)

    @classmethod
    def get_feedbacks(
        cls,
        username: Optional[str],
        page: int,
        size: int,
        db: Session
    ) -> FeedbackPageResponse:
        """
        Get feedbacks with pagination and optional username filter
        
        Args:
            username: Optional username filter
            page: Page number (0-indexed)
            size: Page size
            db: Database session
            
        Returns:
            Paginated feedback response
        """
        # Build query
        query = db.query(Feedback)

        # Apply username filter if provided
        if username and username.strip():
            query = query.filter(Feedback.username == username.strip())

        # Get total count
        total = query.count()

        # Apply ordering and pagination
        feedbacks = query.order_by(Feedback.created_at.desc()) \
            .offset(page * size) \
            .limit(size) \
            .all()

        # Convert to response models
        items = [FeedbackResponse.model_validate(f) for f in feedbacks]

        # Calculate total pages
        total_pages = (total + size - 1) // size if size > 0 else 0

        return FeedbackPageResponse(
            items=items,
            total=total,
            page=page,
            size=size,
            total_pages=total_pages
        )
