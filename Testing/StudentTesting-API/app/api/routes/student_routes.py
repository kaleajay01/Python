from fastapi import APIRouter, Request, HTTPException

from app.schemas.student_schema import (StudentCreate, StudentUpdate, StudentResponse)

router = APIRouter(prefix="/api/student", tags=["Student"])

# GET ALL STUDENT

@router.get("/", response_model=list[StudentResponse])
def get_all_students(request: Request):

    service = request.app.state.student_service

    students = service.get_all_students()

    return [
        {
            "student_id": student.student_id,
            "student_name": student.student_name,
            "age": student.age,
            "address": student.address,
            "mobile_no": student.mobile_no
        }
        for student in students ]
    
# GET STUDENT BY ID
@router.get("/{student_id}", response_model=StudentResponse)
def get_student_by_id(
    student_id: int,
    request: Request
):

    service = request.app.state.student_service
    student = service.get_student_by_id(student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "student_id": student.student_id,
        "student_name": student.student_name,
        "age": student.age,
        "address": student.address,
        "mobile_no": student.mobile_no
    }
   
# CREATE STUDENT
@router.post("/", response_model=StudentResponse)
def create_student(
    student: StudentCreate,
    request: Request
):

    service = request.app.state.student_service

    result = service.create_student(
        student.model_dump()
    )

    return {
        "student_id": result.student_id,
        "student_name": result.student_name,
        "age": result.age,
        "address": result.address,
        "mobile_no": result.mobile_no
    }

# UPDATE STUDENT
@router.put("/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentUpdate, request: Request):

    service = request.app.state.student_service

    result = service.update_student(
        student_id,
        student.model_dump()
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "student_id": result.student_id,
        "student_name": result.student_name,
        "age": result.age,
        "address": result.address,
        "mobile_no": result.mobile_no
    }

# DELETE STUDENT
@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    request: Request
):

    service = request.app.state.student_service

    result = service.delete_student(student_id)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return result