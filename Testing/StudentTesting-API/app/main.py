from fastapi import FastAPI

from .api.routes.student_routes import router as student_router
from .repositories.student_repository import StudentRepository
from .services.student_services import StudentService

app = FastAPI(title="StudentTesting-API",description="Student Testing API",version="1.0")

# Create shared application dependencies
repository = StudentRepository()
app.state.student_service = StudentService(repository)


# Register API routes
app.include_router(student_router)

@app.get("/")
def home():
    return {
        "application": "StudentTesting-API",
        "message": "Welcome to Student Testing API",
        "docs": "/docs"
    }