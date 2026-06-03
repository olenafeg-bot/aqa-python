from sqlalchemy import Table, Column, Integer, ForeignKey
from lesson_21.declarative_base import Base

student_courses = Table(
    "student_courses",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"),primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.id"), primary_key=True)
)
