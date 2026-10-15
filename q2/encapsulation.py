
class CD:
    def __init__(self, campus_head):
        self.__campus_head = campus_head

    def get_campus_head(self):
        return self.__campus_head

    def set_campus_head(self, new_head):
        self.__campus_head = new_head

    def display_head(self):
        print("Campus Director:", self.get_campus_head())

    def display_location(self):
        print("Campus: Zamboanga Peninsula Regional Campus")


class CID(CD):
    def __init__(self, campus_head, division_head,
                 program, school_year, subject_count):
        super().__init__(campus_head)
        self.__division_head = division_head
        self.__program = program
        self.__school_year = school_year
        self.__subject_count = subject_count

    def get_division_head(self):
        return self.__division_head

    def set_division_head(self, value):
        self.__division_head = value

    def get_program(self):
        return self.__program

    def set_program(self, value):
        self.__program = value

    def get_school_year(self):
        return self.__school_year

    def set_school_year(self, value):
        self.__school_year = value

    def get_subject_count(self):
        return self.__subject_count

    def set_subject_count(self, value):
        self.__subject_count = value

    def display_division(self):
        print("CID Division Head:", self.get_division_head())
        print("Academic Program:", self.get_program())
        print("School Year:", self.get_school_year())

    def display_subject_count(self):
        print("Total Subjects:", self.get_subject_count())


class SSD(CD):
    def __init__(self, campus_head, division_head, student_service):
        super().__init__(campus_head)
        self.__division_head = division_head
        self.__student_service = student_service

    def get_division_head(self):
        return self.__division_head

    def set_division_head(self, value):
        self.__division_head = value

    def get_student_service(self):
        return self.__student_service

    def set_student_service(self, value):
        self.__student_service = value

    def display_division(self):
        print("SSD Division Head:", self.get_division_head())

    def display_service(self):
        print("Student Service:", self.get_student_service())


class Academic(CID):
    def __init__(self, campus_head, division_head, program,
                 school_year, subject_count, field):
        super().__init__(
            campus_head, division_head, program,
            school_year, subject_count
        )
        self.__field = field

    def get_field(self):
        return self.__field

    def set_field(self, value):
        self.__field = value

    def display_field(self):
        print("Academic Field:", self.get_field())


class Assessment(CID):
    def __init__(self, campus_head, division_head, program,
                 school_year, subject_count, evaluation_type):
        super().__init__(
            campus_head, division_head, program,
            school_year, subject_count
        )
        self.__evaluation_type = evaluation_type

    def get_evaluation_type(self):
        return self.__evaluation_type

    def set_evaluation_type(self, value):
        self.__evaluation_type = value

    def display_evaluation(self):
        print("Evaluation Type:", self.get_evaluation_type())


class Examination(Assessment):
    def __init__(self, campus_head, division_head, program,
                 school_year, subject_count, evaluation_type,
                 exam_date):
        super().__init__(
            campus_head, division_head, program,
            school_year, subject_count, evaluation_type
        )
        self.__exam_date = exam_date

    def get_exam_date(self):
        return self.__exam_date

    def set_exam_date(self, value):
        self.__exam_date = value

    def display_exam_date(self):
        print("Examination Date:", self.get_exam_date())


class Faculty(CID):
    def __init__(self, campus_head, division_head, program,
                 school_year, subject_count, development_program):
        super().__init__(
            campus_head, division_head, program,
            school_year, subject_count
        )
        self.__development_program = development_program

    def get_development_program(self):
        return self.__development_program

    def set_development_program(self, value):
        self.__development_program = value

    def display_development(self):
        print("Faculty Development:", self.get_development_program())


class StudentWelfare(SSD):
    def __init__(self, campus_head, division_head,
                 student_service, welfare_activity):
        super().__init__(campus_head, division_head, student_service)
        self.__welfare_activity = welfare_activity

    def get_welfare_activity(self):
        return self.__welfare_activity

    def set_welfare_activity(self, value):
        self.__welfare_activity = value

    def display_welfare(self):
        print("Student Welfare Activity:", self.get_welfare_activity())


# OBJECT CREATION

campus = CD("Sir Gallamaso")

curriculum = CID(
    "Sir Gallamaso", "Ma'am Raznee",
    "K-12 Curriculum", "2026-2027", 8
)

student_services = SSD(
    "Sir Gallamaso", "Gamil", "Student Counseling"
)

academic = Academic(
    "Sir Gallamaso", "Ma'am Raznee",
    "K-12 Curriculum", "2026-2027", 8, "Science"
)

assessment = Assessment(
    "Sir Gallamaso", "Ma'am Raznee",
    "K-12 Curriculum", "2026-2027", 8, "Quarterly Examination"
)

examination = Examination(
    "Sir Gallamaso", "Ma'am Raznee",
    "K-12 Curriculum", "2026-2027", 8,
    "Quarterly Examination", "October 20"
)

faculty = Faculty(
    "Sir Gallamaso", "Ma'am Raznee",
    "K-12 Curriculum", "2026-2027", 8, "Teacher Training"
)

welfare = StudentWelfare(
    "Sir Gallamaso", "Gamil",
    "Student Counseling", "Student Wellness"
)


# DISPLAY INFORMATION

print("=== CAMPUS INFORMATION ===")
campus.display_head()
campus.display_location()

print("\n=== CID INFORMATION ===")
curriculum.display_head()
curriculum.display_division()
curriculum.display_subject_count()

print("\n=== SSD INFORMATION ===")
student_services.display_head()
student_services.display_division()
student_services.display_service()

print("\n=== ACADEMIC INFORMATION ===")
academic.display_division()
academic.display_field()

print("\n=== ASSESSMENT INFORMATION ===")
assessment.display_division()
assessment.display_evaluation()

print("\n=== EXAMINATION INFORMATION ===")
examination.display_evaluation()
examination.display_exam_date()

print("\n=== FACULTY INFORMATION ===")
faculty.display_division()
faculty.display_development()

print("\n=== STUDENT WELFARE INFORMATION ===")
welfare.display_division()
welfare.display_welfare()
