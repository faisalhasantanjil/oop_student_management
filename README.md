# School Management System

A Python-based School Management System implementing Object-Oriented Programming concepts. The system manages students, teachers, courses, grades, and attendance records.

## 📚 Classes Overview

### Person (Base Class)
- **Attributes**
  - `__name` (private): Person's full name
  - `__age` (private): Person's age
- **Methods**
  - `get_name()`: Returns person's name
  - `set_name(value)`: Sets person's name with validation
  - `get_age()`: Returns person's age
  - `set_age(value)`: Sets person's age with validation
  - `get_info()`: Returns basic information dictionary

### Student (Inherits from Person)
- **Attributes**
  - Inherits `__name` and `__age` from Person
  - `__student_id` (private): Unique identifier for student
  - `__grades` (private): Dictionary mapping Course objects to letter grades
  - `__courses` (private): List of enrolled Course objects
  - `__attendance` (private): Dictionary tracking daily attendance
- **Methods**
  - `get_point_of_grade(grade)`: Converts letter grades to GPA points
  - `get_student_id()`: Returns student ID
  - `add_course(course)`: Enrolls student in a course
  - `add_grade(course, grade)`: Records letter grade for a course
  - `calculate_gpa()`: Computes GPA on 4.0 scale
  - `mark_attendance(date, attend)`: Records student's attendance
  - `get_attendance()`: Returns attendance record
  - `get_info()`: Returns comprehensive student information

### Teacher (Inherits from Person)
- **Attributes**
  - Inherits `__name` and `__age` from Person
  - `teacher_id`: Unique identifier for teacher
  - `subject`: Subject taught by teacher
  - `__hourly_wage` (private): Teacher's hourly pay rate
  - `__student_attendance` (private): Dictionary tracking students' attendance
- **Methods**
  - `get_hourly_wage()`: Returns hourly wage
  - `set_hourly_wage(value)`: Sets hourly wage with validation
  - `calculate_salary(hours_worked)`: Calculates salary based on hours
  - `mark_attendance(date, records)`: Records attendance for multiple students
  - `get_attendance()`: Returns formatted attendance records
  - `get_info()`: Returns comprehensive teacher information

### Course
- **Attributes**
  - `_course_name`: Name of the course
  - `_course_code`: Unique course identifier
  - `_credits`: Number of credits for the course
- **Methods**
  - `get_course_details()`: Returns course information dictionary

## 🎯 Key Features

- **Grade System**: Uses letter grades (A, A-, B, B-, C, D, F) with 4.0 scale GPA calculation
- **Attendance Tracking**: Both students and teachers can record/view attendance
- **Flexible Date Handling**: Accepts both date objects and ISO format strings for attendance
- **Data Validation**: Implements validation for age, wages, and other inputs
- **Information Access**: Comprehensive get_info() methods for all classes

## 🚀 Usage Example

```python
# Create courses
math = Course("Math", "MAT101", 3)
physics = Course("Physics", "PHY101", 4)

# Create students
student = Student("Abdul", 20, "S123")
student1 = Student("Hakim", 21, "S124")

# Add courses and grades
student.add_course(math)
student.add_course(physics)
student.add_grade(math, 'A')
student.add_grade(physics, 'A-')

# Create teacher
teacher = Teacher("Dr. Smith", 45, "T98765", "Mathematics")

# Mark attendance
today = datetime.now().date()
attendance_records = {student: True, student1: False}
teacher.mark_attendance(today, attendance_records)
teacher.mark_attendance("2024-10-26", {student: True, student1: True})

# Print information
print("Student Info:", student.get_info())
print("Teacher Info:", teacher.get_info())
print(f"Student GPA: {student.calculate_gpa()}")
print(f"Teacher Salary: {teacher.calculate_salary(40)} Tk")
print(f"Attendance: {teacher.get_attendance()}")
```

## 🔑 Implementation Details

### Encapsulation
- Private attributes using double underscore (`__`)
- Getter/Setter methods for controlled access
- Protected course attributes using single underscore (`_`)

### Inheritance
- `Student` and `Teacher` inherit from `Person`
- Override of `get_info()` method in child classes

### Polymorphism
- Different implementations of `mark_attendance()` in Student and Teacher classes
- Flexible date handling in attendance methods

### Composition
- Course objects composed within Student class
- Complex attendance tracking system using nested data structures

## 📝 Notes
- Default hourly wage for teachers is set to 30.0
- GPA is calculated using a standard 4.0 scale
- Attendance can be marked using both date objects and strings
