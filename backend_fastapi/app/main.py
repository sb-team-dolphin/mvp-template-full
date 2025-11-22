from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from .database import create_tables
from .routers import feedback_router, health_router
from .config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event handler for startup and shutdown"""
    # Startup: Create database tables
    print("Creating database tables...")
    create_tables()
    print("Database tables created successfully!")
    yield
    # Shutdown: cleanup if needed
    print("Shutting down...")


# Create FastAPI application
app = FastAPI(
    title="MyApp Backend API",
    description="Demo Backend Application API Documentation",
    version="1.0.0",
    docs_url="/swagger-ui.html",  # Swagger UI endpoint (same as Spring Boot)
    openapi_url="/api-docs",      # OpenAPI JSON endpoint (same as Spring Boot)
    redoc_url="/redoc",           # ReDoc UI endpoint
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(feedback_router)
app.include_router(health_router)


@app.get("/", tags=["Root"])
def root():
    """Root endpoint"""
    return {
        "message": "Welcome to MyApp Backend API",
        "docs": "/swagger-ui.html",
        "openapi": "/api-docs",
        "health": "/health"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=settings.server_port,
        reload=True
    )
