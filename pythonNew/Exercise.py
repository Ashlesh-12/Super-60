from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship, create_engine, Session, select

class Department(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    building: Optional[str] = None

    courses: List["Course"] = Relationship(back_populates="department")

class StudentCourseLink(SQLModel, table=True):
    student_id: int = Field(default=None, foreign_key="student.id", primary_key=True)
    course_id: int = Field(default=None, foreign_key="course.id", primary_key=True)
    enrollment_date: Optional[datetime] = None
    grade: Optional[str] = None

class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: str = Field(unique=True)

    courses: List["Course"] = Relationship(back_populates="students", link_model=StudentCourseLink)

class Course(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    code: str = Field(unique=True)
    department_id: Optional[int] = Field(default=None, foreign_key="department.id")

    department: Optional[Department] = Relationship(back_populates="courses")
    students: List[Student] = Relationship(back_populates="courses", link_model=StudentCourseLink)

DATABASE_URL = "sqlite:///university.db"
engine = create_engine(DATABASE_URL, echo=True)  # echo=True logs SQL statements

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_department(name: str, building: Optional[str] = None):
    with Session(engine) as session:
        department = Department(name=name, building=building)
        session.add(department)
        session.commit()
        session.refresh(department)
        return department

def create_student(first_name: str, last_name: str, email: str):
    with Session(engine) as session:
        student = Student(first_name=first_name, last_name=last_name, email=email)
        session.add(student)
        session.commit()
        session.refresh(student)
        return student

def create_course(title: str, code: str, department_id: Optional[int] = None):
    with Session(engine) as session:
        course = Course(title=title, code=code, department_id=department_id)
        session.add(course)
        session.commit()
        session.refresh(course)
        return course

def get_department_by_name(name: str):
    with Session(engine) as session:
        statement = select(Department).where(Department.name == name)
        return session.exec(statement).first()

def get_student_by_email(email: str):
    with Session(engine) as session:
        statement = select(Student).where(Student.email == email)
        return session.exec(statement).first()

def get_course_by_code(code: str):
    with Session(engine) as session:
        statement = select(Course).where(Course.code == code)
        return session.exec(statement).first()

def list_all_students():
    with Session(engine) as session:
        return session.exec(select(Student)).all()

def list_all_courses():
    with Session(engine) as session:
        return session.exec(select(Course)).all()

def list_all_departments():
    with Session(engine) as session:
        return session.exec(select(Department)).all()

def update_student_email(student_id: int, new_email: str):
    with Session(engine) as session:
        student = session.get(Student, student_id)
        if student:
            student.email = new_email
            session.add(student)
            session.commit()
            session.refresh(student)
        return student

def delete_course(code: str):
    with Session(engine) as session:
        course = get_course_by_code(code)
        if course:
            session.delete(course)
            session.commit()
            return True
        return False

def enroll_student(student_id: int, course_id: int, enrollment_date: Optional[datetime] = None):
    with Session(engine) as session:
        student = session.get(Student, student_id)
        course = session.get(Course, course_id)

        if not student or not course:
            return "Student or Course not found"

        # Check if already enrolled
        for enrolled_course in student.courses:
            if enrolled_course.id == course_id:
                return "Student already enrolled in this course"

        link = StudentCourseLink(
            student_id=student_id,
            course_id=course_id,
            enrollment_date=enrollment_date or datetime.now()
        )
        session.add(link)
        session.commit()
        return "Enrollment successful"

def get_courses_for_student(student_id: int):
    with Session(engine) as session:
        student = session.get(Student, student_id)
        if not student:
            return "Student not found"
        
        for course in student.courses:
            print(f"{course.title} ({course.code})")
        return student.courses

def get_students_in_course(course_id: int):
    with Session(engine) as session:
        course = session.get(Course, course_id)
        if not course:
            return "Course not found"
        
        for student in course.students:
            print(f"{student.first_name} {student.last_name}")
        return course.students

def set_enrollment_grade(student_id: int, course_id: int, grade: str):
    with Session(engine) as session:
        statement = select(StudentCourseLink).where(
            StudentCourseLink.student_id == student_id,
            StudentCourseLink.course_id == course_id
        )
        link = session.exec(statement).first()
        if not link:
            return "Enrollment not found"

        link.grade = grade
        session.add(link)
        session.commit()
        return "Grade updated"

def unenroll_student(student_id: int, course_id: int):
    with Session(engine) as session:
        statement = select(StudentCourseLink).where(
            StudentCourseLink.student_id == student_id,
            StudentCourseLink.course_id == course_id
        )
        link = session.exec(statement).first()
        if not link:
            return "Enrollment not found"

        session.delete(link)
        session.commit()
        return "Unenrolled successfully"


if __name__ == "__main__":
    from datetime import datetime

    create_db_and_tables()

    cs = create_department("Computer Science", "Building A")
    math = create_department("Mathematics", "Building B")

    course1 = create_course("Intro to Python", "CS101", cs.id)
    course2 = create_course("Data Structures", "CS102", cs.id)
    course3 = create_course("Calculus I", "MATH101", math.id)

    student1 = create_student("Arshith", "CP", "arshith@example.com")
    student2 = create_student("Cristiano", "ROnaldo", "cr7@example.com")

    print(enroll_student(student1.id, course1.id))
    print(enroll_student(student1.id, course2.id))
    print(enroll_student(student2.id, course1.id))
    print(enroll_student(student2.id, course3.id))

    print("\nCourses for Arshith:")
    get_courses_for_student(student1.id)

    print("\nStudents in CS101:")
    get_students_in_course(course1.id)

    print(set_enrollment_grade(student1.id, course1.id, "A"))

    print(unenroll_student(student2.id, course1.id))

    print("\nStudents in CS101 after unenrollment:")
    get_students_in_course(course1.id)

    print(update_student_email(student2.id, "cristiano@example.com"))

    print(delete_course("MATH101"))

    print("\nAll Students:")
    for s in list_all_students():
        print(f"{s.id}: {s.first_name} {s.last_name} - {s.email}")