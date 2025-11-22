from sqlalchemy import Column, BigInteger, String, DateTime
from sqlalchemy.sql import func
from ..database import Base


class Feedback(Base):
    """Feedback model representing user feedback"""

    __tablename__ = "feedbacks"

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)
    username = Column(String(100), nullable=True)
    message = Column(String(1000), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return f"<Feedback(id={self.id}, username={self.username})>"
