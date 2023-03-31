from fast_api import FastAPI
from Dataset import students
app = FastAPI()

@app.get("/")
def index():
    return {"name" : "M.Haris Imran" ,
            "Title" : "Api Generator"    
        }

@app.get("/get_student/{student_id}")
def get_student(student_id:int):
    return students[student_id]

@app.post("/post_student/{student_id}")
def post_student(student_id:int):
    return students[student_id]