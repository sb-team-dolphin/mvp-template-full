from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from typing import Optional

from ..database import get_db
from ..schemas import ApiResponse, FeedbackCreateRequest, FeedbackResponse, FeedbackPageResponse
from ..services.feedback import FeedbackService

router = APIRouter(prefix="/api/feedbacks", tags=["Feedback"])


@router.post(
    "",
    response_model=ApiResponse[FeedbackResponse],
    status_code=status.HTTP_201_CREATED,
    summary="피드백 생성",
    description="새로운 피드백을 생성합니다.",
    responses={
        201: {"description": "피드백 생성 성공"},
        400: {"description": "잘못된 요청"}
    }
)
def create_feedback(
    request: FeedbackCreateRequest,
    db: Session = Depends(get_db)
):
    """Create a new feedback"""
    feedback = FeedbackService.create_feedback(request, db)
    return ApiResponse.success_response(feedback)


@router.get(
    "",
    response_model=ApiResponse[FeedbackPageResponse],
    summary="피드백 목록 조회",
    description="페이지네이션 및 사용자명 필터를 사용하여 피드백 목록을 조회합니다.",
    responses={
        200: {"description": "조회 성공"}
    }
)
def get_feedbacks(
    page: int = Query(0, ge=0, description="페이지 번호 (0부터 시작)"),
    size: int = Query(20, ge=1, le=100, description="페이지 크기 (1-100)"),
    username: Optional[str] = Query(None, description="사용자명 필터 (선택사항)"),
    db: Session = Depends(get_db)
):
    """Get feedbacks with pagination and optional username filter"""
    feedbacks = FeedbackService.get_feedbacks(username, page, size, db)
    return ApiResponse.success_response(feedbacks)
