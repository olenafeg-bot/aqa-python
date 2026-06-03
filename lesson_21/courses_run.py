from DB_Connection import SQLAlchemyClient

from lesson_21.courses_table import Course
from lesson_21.students_table import Student
from lesson_21.student_courses import student_courses


import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

logger = logging.getLogger(__name__)

try:
    sqlalchemy_client = SQLAlchemyClient()


    sqlalchemy_client.create_all_tables()
    sqlalchemy_client.session

    course_python = Course(name='Python Programming')
    course_java = Course(name='Java Programming')
    course_javascript = Course(name='Javascript Programming')
    course_management = Course(name='Management')
    course_qa = Course(name='QA')


    sqlalchemy_client.session.add_all([course_java, course_javascript, course_python, course_management, course_qa])
    sqlalchemy_client.session.commit()
    logger.info("Courses added successfully ")

    student_1 = Student(first_name='Vitaliy', last_name='Derevach', age=25)
    student_2 = Student(first_name='Tamara', last_name='Kar', age=19)
    student_3 = Student(first_name='Olena', last_name='Smith', age=22)
    student_4 = Student(first_name='Lucy', last_name='Santa', age=24)
    student_5 = Student(first_name='Nathan', last_name='James', age=26)

    sqlalchemy_client.session.add_all([student_1, student_2, student_3, student_4, student_5])
    sqlalchemy_client.session.commit()

    logger.info("Students added successfully")

    # connections
    student_1.course.extend([course_javascript, course_python])
    student_2.course.append(course_java)
    student_3.course.append(course_management)
    student_4.course.append(course_qa)
    student_5.course.extend([course_qa, course_management])
    sqlalchemy_client.session.add_all([student_1, student_2, student_3, student_4, student_5])
    sqlalchemy_client.session.commit()




    # query 1.
    course = sqlalchemy_client.session.query(Course).filter_by(name='Python Programming').first()

    logger.info(f"Students in course: {course.name}")

    for student in course.students:
        logger.info(f"{student.first_name} {student.last_name}, age={student.age}")

#Add new  student

    new_student = Student(first_name='Vitaliy', last_name='Soroka', age=35)
    new_student.courses = [course_java, course_javascript]
    sqlalchemy_client.session.add(new_student)
    sqlalchemy_client.session.commit()
    logger.info(f"Students {new_student.first_name} {new_student.last_name}")

#query 2

    qa_course = sqlalchemy_client.session.query(Course).filter_by(name='QA').first()

    logger.info(f"Students in course: {qa_course.name}")

    for student in course_qa.students:
        logger.info(f"{student.first_name} {student.last_name}, age={student.age}")

#query 3

    students = sqlalchemy_client.session.query(Student).join(Student.course).filter(Course.name == "Java Programming").all()
    for student in students:
        logger.info(student)
    logger.info(f"Found {len(students)} students")

#update info about student
    student = sqlalchemy_client.session.query(Student) \
        .filter(Student.first_name == "Vitaliy", Student.last_name == "Derevach") \
        .first()

    if student:
        student.age = 30
        sqlalchemy_client.session.commit()
        logger.info(f"Updated student: {student.first_name} {student.last_name}, age={student.age}")

#deletion of the student
    student = sqlalchemy_client.session.query(Student)\
        .filter(Student.first_name == "Nathan", Student.last_name == "James")\
        .first()

    if student:
        sqlalchemy_client.session.delete(student)
        sqlalchemy_client.session.commit()
        logger.info(f"Deleted student: {student.first_name} {student.last_name}")

except Exception as e:
    logger.exception("Something went wrong")
    sqlalchemy_client.close_connection()