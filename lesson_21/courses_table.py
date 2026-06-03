from sqlalchemy import Column, String, Boolean, Integer
from lesson_21.declarative_base import Base
from sqlalchemy.orm import relationship

from lesson_21.student_courses import student_courses


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))

    students = relationship("Student", secondary=student_courses, back_populates="course")