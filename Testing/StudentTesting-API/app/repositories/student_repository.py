import mysql.connector
from app.models.student import Student

class StudentRepository:
    
    def __init__(self):
        
       self.connection = mysql.connector.connect(host="localhost", user="root", password="password", database="student_db")
       
       # GET ALL STUDENTS
    def get_all(self):

        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        cursor.close()
        return [Student(**row) for row in rows]
    
    # GET STUDENT BY ID
    def get_by_id(self, student_id: int):

        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
        row = cursor.fetchone()
        cursor.close()

        if row is None:
            return None

        return Student(**row)


    # CREATE STUDENT
    def create(self, student_data: dict):

        cursor = self.connection.cursor()
        query = """
            INSERT INTO students (student_name, age, address, mobile_no)VALUES (%s, %s, %s, %s) """

        values = (student_data["student_name"],student_data["age"],student_data["address"],student_data["mobile_no"])

        cursor.execute(query, values) 
        self.connection.commit()
        student_id = cursor.lastrowid
        cursor.close()

        return self.get_by_id(student_id)
    
    
     # UPDATE STUDENT
    def update(self, student_id: int, student_data: dict):

        cursor = self.connection.cursor()

        query = """ UPDATE students SET student_name = %s, age = %s,address = %s, mobile_no = %s WHERE student_id = %s"""

        values = (student_data["student_name"],student_data["age"],student_data["address"],student_data["mobile_no"],student_id)  
        cursor.execute(query, values)
        affected_rows = cursor.rowcount
        self.connection.commit()
        cursor.close()

        if affected_rows == 0:
            return None

        return self.get_by_id(student_id)
    
     # DELETE STUDENT
    def delete(self, student_id: int):

        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM students WHERE student_id = %s",(student_id,))
        affected_rows = cursor.rowcount
        self.connection.commit()
        cursor.close()

        if affected_rows == 0:
            return None

        return {
            "message": "Student deleted successfully"
        }