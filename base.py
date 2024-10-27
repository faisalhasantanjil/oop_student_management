from datetime import datetime, date

class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def set_name(self, value: str):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self.__name = value

    def get_age(self) -> int:
        return self.__age

    def set_age(self, value: int):  # Fixed method name from ser_age to set_age
        if value < 1:
            raise ValueError("Age must be a valid number")
        self.__age = value

    def get_info(self):
        return {
            "name": self.__name,
            "age": self.__age
        }


class Course:
    def __init__(self, course_name: str, course_code: str, credits: int):
        self._course_name = course_name
        self._course_code = course_code
        self._credits = credits

    def get_course_details(self):
        return {
            "course_name": self._course_name,
            "course_code": self._course_code,
            "credits": self._credits
        }

class Student(Person):
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.__student_id = student_id
        self.__grades: dict[Course, str] = {}
        self.__courses: list[Course] = []
        self.__attendance: dict[date, bool] = {}

    def get_point_of_grade(self, grade: str):
        points = {
            'A': 4.00,
            'A-': 3.50,
            'B': 3.00,
            'B-': 2.50,
            'C': 2.25,
            'D': 2.00,
            'F': 0.00,
        }
        return points.get(grade, 0.0)  # Use get to avoid KeyError

    def get_student_id(self) -> str:
        return self.__student_id

    def add_course(self, course: Course) -> None:
        if course not in self.__courses:
            self.__courses.append(course)
        else:
            raise ValueError("Already Enrolled in the Course")

    def add_grade(self, course: Course, grade:str) -> None:
        if course not in self.__courses:
            raise ValueError("Student is not enrolled in this course")

        self.__grades[course] = grade

    def calculate_gpa(self) -> float:
        if not self.__grades:
            return 0.0

        total_points = 0
        total_credits = 0

        for course, grade in self.__grades.items():
            # Convert percentage to 4.0 scale
            total_points += self.get_point_of_grade(grade) * course._credits
            total_credits += course._credits

        return round(total_points / total_credits, 2) if total_credits > 0 else 0.0

    def mark_attendance(self, attendance_date: date, attend: bool):
        self.__attendance[attendance_date] = attend

    def get_attendance(self):
        return self.__attendance

    def get_info(self):
        basic_info = super().get_info()
        return {
            **basic_info,
            "student_id": self.__student_id,
            "enrolled_courses": [course._course_name for course in self.__courses],
            "gpa": self.calculate_gpa()
        }

class Teacher(Person):
    def __init__(self, name: str, age: int, teacher_id: str, subject: str, hourly_wage: float = 30.0):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.subject = subject
        self.__hourly_wage = hourly_wage
        self.__student_attendance: dict[date, list[tuple[Student, bool]]] = {}  # {date: [(Student, status)]}

    def get_hourly_wage(self):
        return self.__hourly_wage

    def set_hourly_wage(self, hourly_wage: float):
        if hourly_wage < 0:
            raise ValueError('Value must be a positive number')
        self.__hourly_wage = hourly_wage

    def calculate_salary(self, hours_worked: float) -> float:
        return round(hours_worked * self.__hourly_wage, 2)

    def mark_attendance(self, attend_date: date|str, attendance_records: dict[Student, bool]) -> None:
        # Initialize the date in attendance record if not exists
        print(type(attend_date))
        attend_date = datetime.fromisoformat(attend_date).date() if isinstance(attend_date, str) else attend_date
        if attend_date not in self.__student_attendance:
            self.__student_attendance[attend_date] = []

        # Mark attendance for each student
        for student, status in attendance_records.items():
            # Update teacher's record
            self.__student_attendance[attend_date].append((student, status))
            # Update student's own attendance record
            student.mark_attendance(attend_date, status)

    def get_attendance(self):
        attendance_dict = self.__student_attendance  # Assuming your data is stored in a dictionary

        attendance_list = []
        for dates, student_attendances in attendance_dict.items():
            students_with_attendance = []
            for student, attended in student_attendances:
                students_with_attendance.append(f"{student.get_student_id()} - {attended}")
            attendance_list.append(f"{dates}: {', '.join(students_with_attendance)}")
        return attendance_list

    def get_info(self):
        basic_info = super().get_info()
        return {
            **basic_info,
            "teacher_id": self.teacher_id,
            "subject": self.subject,
            "hourly_wage": self.get_hourly_wage()
        }

# Example usage
math = Course("Math", "MAT101", 3)
physics = Course("Physics", "PHY101", 4)

# Create student
student = Student("Abdul", 20, "S123")
student1 = Student("Hakim", 21, "S124")
student.add_course(math)
student.add_course(physics)
student.add_grade(math, 'A')  # Use letter grades
student.add_grade(physics, 'A-')  # Use letter grades

# Create teacher
teacher = Teacher("Dr. Smith", 45, "T98765", "Mathematics")
print("Teacher Salary for 40 hours:", teacher.calculate_salary(40))

# Mark attendance
today = datetime.now().date()
attendance_records = {student: True, student1: False}
attendance_records2 = {student: True, student1: True}
teacher.mark_attendance(today, attendance_records)
teacher.mark_attendance("2024-10-26", attendance_records2)

# Print information
print("Student Info:", student.get_info())
print("Teacher Info:", teacher.get_info())
print(f"Student GPA: {student.calculate_gpa()}")
print(f"Teacher Salary: {teacher.calculate_salary(40)} Tk")
print(f"Attendance: {teacher.get_attendance()}")
print(f"Student Attendance: {student.get_attendance()}")
