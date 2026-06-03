from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, Table
from lesson_21.declarative_base import Base
from sqlalchemy.orm import relationship
from lesson_21.student_courses import student_courses
#from student_courses import Table

# student_courses = Table(
#     "student_courses",
#     Base.metadata,
#     Column("student_id", Integer, ForeignKey("students.id")),
#     Column("course_id", Integer, ForeignKey("courses.id"))
# )


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    age = Column(Integer)


    course = relationship("Course", secondary=student_courses, back_populates="students")
