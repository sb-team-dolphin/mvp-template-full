from fastapi import APIRouter
import psutil
from datetime import datetime

router = APIRouter(tags=["Health"])


@router.get(
    "/health",
    summary="기본 헬스 체크",
    description="ALB와 ECS에서 사용하는 헬스 체크 엔드포인트"
)
def health():
    """Basic health check endpoint"""
    return {
        "status": "UP",
        "service": "myapp-backend",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat()
    }


@router.get(
    "/health/detail",
    summary="상세 헬스 체크",
    description="시스템 메모리 및 프로세서 정보를 포함한 상세 헬스 체크"
)
def health_detail():
    """Detailed health check with system information"""
    # Get system information
    memory = psutil.virtual_memory()
    cpu_percent = psutil.cpu_percent(interval=1)

    return {
        "status": "UP",
        "service": "myapp-backend",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat(),
        "system": {
            "totalMemory": f"{memory.total / (1024 * 1024):.0f} MB",
            "availableMemory": f"{memory.available / (1024 * 1024):.0f} MB",
            "usedMemory": f"{memory.used / (1024 * 1024):.0f} MB",
            "memoryPercent": f"{memory.percent}%",
            "cpuPercent": f"{cpu_percent}%",
            "processors": psutil.cpu_count()
        }
    }
