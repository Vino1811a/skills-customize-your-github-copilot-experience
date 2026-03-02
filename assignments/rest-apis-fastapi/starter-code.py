"""
Starter code for Building REST APIs with FastAPI assignment.

This file provides the basic structure to get started building a REST API.
Complete the TODO sections to implement the required functionality.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI application
app = FastAPI(
    title="Student API",
    description="A simple REST API for managing students",
    version="1.0.0"
)

# TODO: Define a Pydantic model for Student data
# Should include: id (int), name (str), email (str), grade (int)
class Student(BaseModel):
    pass


# In-memory "database" to store students
students_db = []
next_id = 1


@app.get("/")
async def root():
    """Welcome endpoint"""
    # TODO: Return a welcome message as a dictionary
    pass


@app.get("/students")
async def get_students() -> List[Student]:
    """Get list of all students"""
    # TODO: Return all students from the database
    pass


@app.post("/students", status_code=201)
async def create_student(student: Student) -> Student:
    """Create a new student"""
    # TODO: Add the student to the database with a new ID
    # Return the created student with ID
    pass


@app.get("/students/{student_id}")
async def get_student(student_id: int) -> Student:
    """Get a specific student by ID"""
    # TODO: Find and return student with given ID
    # Raise HTTPException with 404 if not found
    pass


@app.put("/students/{student_id}")
async def update_student(student_id: int, student: Student) -> Student:
    """Update an existing student"""
    # TODO: Find student by ID and update their information
    # Raise HTTPException with 404 if not found
    pass


@app.delete("/students/{student_id}", status_code=204)
async def delete_student(student_id: int):
    """Delete a student"""
    # TODO: Remove student from database
    # Raise HTTPException with 404 if not found
    pass


# To run this server, use: uvicorn starter-code:app --reload
