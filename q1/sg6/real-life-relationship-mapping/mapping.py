class Student:
    def __init__(self, name: str):
        self.name: str = name


class Course:
    def __init__(self, name: str):
        self.name: str = name
        self.students: list[Student] = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)


# Example
course = Course("Computer Science")

student1 = Student("Jesse")
student2 = Student("Alex")

course.add_student(student1)
course.add_student(student2)

print(course.name)

for student in course.students:
    print(student.name)
