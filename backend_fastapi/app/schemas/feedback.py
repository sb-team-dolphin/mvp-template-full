from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class FeedbackCreateRequest(BaseModel):
    """Request schema for creating feedback"""
    username: Optional[str] = Field(None, max_length=100, description="사용자 이름 (최대 100자)")
    message: str = Field(..., min_length=1, max_length=1000, description="피드백 메시지 (필수, 최대 1000자)")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "username": "홍길동",
                "message": "서비스가 정말 좋습니다!"
            }
        }
    )


class FeedbackResponse(BaseModel):
    """Response schema for feedback"""
    id: int
    username: Optional[str]
    message: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class FeedbackPageResponse(BaseModel):
    """Paginated feedback response"""
    items: list[FeedbackResponse]
    total: int
    page: int
    size: int
    total_pages: int
