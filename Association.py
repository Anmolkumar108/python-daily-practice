                
class Student:
    def __init__(self, student_id, name, course_list=None):
        self.student_id = student_id
        self.name = name
        self.courses = []
        for course in course_list or []:
            self.enroll_course(course)

    def Input_Show(self):
        self.student_id = int(input("Enter Student I'D: "))
        self.name = input("Enter Student Name: ")
    
    def enroll_course(self, course):
        if any(enrolled_course.course_id == course.course_id for enrolled_course in self.courses):
            return False

        self.courses.append(course)
        if not any(student.student_id == self.student_id for student in course.students):
            course.students.append(self)
        return True

    def display_courses(self):
        print(f"Courses for {self.name}:")
        if not self.courses:
            print("No courses enrolled.")
            return
        for course in self.courses:
            print(f"{course.course_id}: {course.name}")

    def check_Course(self, course=None):
        self.display_courses()


class Course:
    def __init__(self, course_id, name, duration):
        self.course_id = course_id
        self.name = name
        self.duration = duration
        self.students = []

    def Input_Show(self):
        self.course_id = int(input("Enter Course ID: "))
        self.name = input("Enter Course Name: ")
        self.duration = int(input("Enter Duration: "))

    def display_students(self):
        print(f"Students enrolled in {self.name}:")
        if not self.students:
            print("No students enrolled.")
            return
        for student in self.students:
            print(f"{student.student_id}: {student.name}")
