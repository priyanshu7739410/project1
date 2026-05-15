from fastapi import FastAPI
from pydantic import BaseModel
import database

app = FastAPI()

submissions = []

class Submission(BaseModel):
    leetcode_id: int
    language: str
    code: str

@app.get("/")
def home():
    return {"message": "Home"}

@app.get("/problem/{leetcode_id}")
def get_problem(leetcode_id: int):

    problems = {
        200: "Number of Islands",
        994: "Rotting Oranges",
        733: "Flood Fill"
    }

    return {
        "leetcode_id": leetcode_id,
        "title": problems.get(leetcode_id, "Problem Not Found")
    }

@app.post("/submit")
def submit_code(submission: Submission):

    submissions.append(submission.dict())

    return {
        "message": "Submission stored",
        "total_submissions": len(submissions)
    }

@app.get("/submissions")
def get_submissions():

    return {
        "submissions": submissions
    }