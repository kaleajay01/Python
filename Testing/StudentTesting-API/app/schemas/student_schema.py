from pydantic import BaseModel, Field

class StudentCreate(BaseModel):
    student_name: str = Field(min_length=2, max_length=100)
    age: int = Field(gt=0)
    address: str = Field(min_length=2, max_length=100)
    mobile_no: float = Field(gt=0)
    
class StudentUpdate(StudentCreate):
    pass


class StudentResponse(StudentCreate):
    student_id: int
    
    
    
    