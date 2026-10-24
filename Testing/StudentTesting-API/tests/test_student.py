from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# GET ALL STUDENT
def test_get_all_students():

    response = client.get("/api/student/")

    assert response.status_code == 200
    assert len(response.json()) >= 13
    
# GET STUDENT BY ID
def test_get_student_by_id():

    response = client.get("/api/student/54")

    assert response.status_code == 200
    assert response.json()["student_id"] == 54
    
# GET STUDENT NOT FOUND
def test_get_student_not_found():

    response = client.get("/api/student/100")

    assert response.status_code == 404
    
# CREATE STUDENT
def test_create_student():

    student = {
        "student_name": "John Doe",
        "age": 20,
        "address": "123 Main St",
        "mobile_no": 1234567890
    }
    
    response = client.post(
        "/api/student/",
        json=student
    )

  #tsting 
    assert response.status_code == 200
    assert response.json()["student_name"] == "John Doe"
    
    
# UPDATE STUDENT
def test_update_student():
    
    student = {
        "student_name": "Jhon Updated",
        "age": 25,
        "address": "12 Main St",
        "mobile_no": 9874561230
    }
    
    response = client.put(
        "/api/student/54",
        json=student
    )
  ##testing
    assert response.status_code == 200
    assert response.json()["student_name"] == "Jhon Updated"
        
   
# DELETE STUDENT
def test_delete_student():

    response = client.delete("/api/student/54")
 ##testing
    assert response.status_code == 200