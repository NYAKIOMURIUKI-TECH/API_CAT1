#NYAKIO NDAMBIRI ESTHER ICS 3A CAT 1 QUESTION2: ONLINE LEARNINGG SYSTEM
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments= {}

    def add_assignment(self, assignments, grade):
        self.assignments[assignments] =grade
    
    def display_grades(self):
        print(f"{self.name}'s grades: ")
        for assignment, grade in self.assignments.items():
            print(f"{assignment}: {grade}")

class Instructor:
    def __init__(self, name, course_name):
        self.name =name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def assign_grade(self, student_id, assignment, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment(assignment, grade)
                print(f"Assigned {grade} to {student.name} for {assignment}")
                return
        print("Student not found.")

    def display_student_grades(self):
        print(f"Grades for {self.course_name}:")
        for student in self.students:
            student.display_grades()

#examples        
student1 = Student("Andrew", 101)
student2 = Student("Nyakio", 102)
instructor = Instructor("Dr. K", "Computer Science")

instructor.add_student(student1)
instructor.add_student(student2)

instructor.assign_grade(101, "Assignment 1", 85)
instructor.assign_grade(102, "Assignment 1", 77)
instructor.display_student_grades()
        