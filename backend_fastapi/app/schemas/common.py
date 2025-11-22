from typing import TypeVar, Generic, Optional, List
from pydantic import BaseModel

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    """Generic API response wrapper"""
    success: bool = True
    data: Optional[T] = None
    error: Optional[str] = None

    @classmethod
    def success_response(cls, data: T):
        """Create a successful response"""
        return cls(success=True, data=data, error=None)

    @classmethod
    def error_response(cls, error: str):
        """Create an error response"""
        return cls(success=False, data=None, error=error)


class PageResponse(BaseModel, Generic[T]):
    """Generic pagination response"""
    items: List[T]
    total: int
    page: int
    size: int
    total_pages: int

    @classmethod
    def create(cls, items: List[T], total: int, page: int, size: int):
        """Create a pagination response"""
        total_pages = (total + size - 1) // size if size > 0 else 0
        return cls(
            items=items,
            total=total,
            page=page,
            size=size,
            total_pages=total_pages
        )
