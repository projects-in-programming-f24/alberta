from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import ObjectId
from typing import List
import os
from dotenv import load_dotenv
import uvicorn

load_dotenv()

app = FastAPI()

MONGODB_URI = os.getenv('MONGODB_URI')
client = MongoClient(MONGODB_URI)
db = client.get_default_database()
courses_collection = db['course']

# I am not defining my data models here. An LLM will do this for you and probably slow down prototyping...
@app.get("/courses/", response_model=List[dict])
def get_courses():
    courses = list(courses_collection.find())
    return [
        {"id": str(course["_id"]), 
         "code": course["code"], 
         "title": course["title"],
         "meeting times": course["meetingTimes"],
        } 
        for course in courses
    ]

# we can make this even simplier if we want:
# @app.get("/courses/")
# def get_courses():
#     courses = list(courses_collection.find())
#     for course in courses:
#         course['_id'] = str(course['_id'])
#     return courses


@app.get("/courses/{course_id}")
def get_course(course_id: str):
    course = courses_collection.find_one({"_id": ObjectId(course_id)})
    if course:
        return {
            "id": str(course["_id"]),
            "code": course["code"],
            "title": course["title"],
        }
    raise HTTPException(status_code=404, detail="Course not found")

@app.post("/courses/")
def create_course(course: dict):
    result = courses_collection.insert_one(course)
    new_course = courses_collection.find_one({"_id": result.inserted_id})
    return {
        "id": str(new_course["_id"]),
        "code": new_course["code"],
        "title": new_course["title"]
    }

@app.put("/courses/{course_id}")
def update_course(course_id: str, course: dict):
    result = courses_collection.update_one({"_id": ObjectId(course_id)}, {"$set": course})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Course not found")
    updated_course = courses_collection.find_one({"_id": ObjectId(course_id)})
    return {
        "id": str(updated_course["_id"]),
        "code": updated_course["code"],
        "title": updated_course["title"]
    }

@app.delete("/courses/{course_id}")
def delete_course(course_id: str):
    result = courses_collection.delete_one({"_id": ObjectId(course_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"message": "Course deleted successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)