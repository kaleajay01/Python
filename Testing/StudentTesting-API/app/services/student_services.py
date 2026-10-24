from app.repositories.student_repository import StudentRepository

class StudentService:
    
    def __init__(self,repository: StudentRepository):
        self.repository = repository
        
     # GET ALL STDUENT
    def get_all_students(self):
        return self.repository.get_all()
      # GET STUDENT BY ID
    def get_student_by_id(self, student_id: int):
        return self.repository.get_by_id(student_id)
    # CREATE STUDENT
    def create_student(self, student_data: dict):
        return self.repository.create(student_data)
     # UPDATE STUDENT
    def update_student(self, student_id: int, student_data: dict):
         return self.repository.update(student_id, student_data)
        # DELETE STUDENT
    def delete_student(self, student_id: int):
        return self.repository.delete(student_id)