from fastapi import FastAPI, Path
from typing import Optional 
from pydantic import BaseModel

app = FastAPI()

students ={
    1:{
        "name":"Leslie",
        "age": 27,
        "year":"2025"

    }
}

class Student(BaseModel):
    name: str
    age: int
    year: int

class UpdateStudent(BaseModel):
     name: Optional[str]=   None
     age: Optional[int]=None
     year: Optional[int]=None

@app.get("/")
def index():
    return{"name":"Leslie"}

#path parameter

@app.get("/students/{student_id}")
def get_student(student_id: int = Path( description="The ID of the student to retrieve")):
        
        return students[student_id]

#query parameter
@app.get("/get-by-name")
def get_student(*, name: Optional[str] =None, test:str):
      for student_id in students:
            if students[student_id]["name"]==name:
                return students[student_id]
      return{"Data":"Not Found"}
    

@app.post("/create-student/{student_id}")
def create_student(student_id:int, student: Student):
    if student_id in students:
        return{"Error":"Student with this ID already exists"}
    students[student_id]=student
    return students[student_id]


@app.put("/update-student/{student_id}")
def update_student(student_id:int, student:UpdateStudent):
     if student_id not in students:
          return{"Error":"Student does not exist"}
     
     if student.name != None:
          students[student_id].name =student.name

     if student.age != None:
          students[student_id].age =student.age

     if student.year != None:
          students[student_id].year =student.year

     return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return{"Error":"Student does not exist"}
    
    del students[student_id]
    return{"Message":"Student deleted successfully"}

 