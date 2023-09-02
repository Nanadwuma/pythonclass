'''class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def average_score(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)


class GradingSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def get_student_average(self, student):
        return student.average_score()

    def get_class_average(self):
        if not self.students:
            return 0
        total_scores = sum(student.average_score() for student in self.students)
        return total_scores / len(self.students)


# Example usage
grading_system = GradingSystem()

# Create students
student1 = Student("John")
student2 = Student("Alice")
student3 = Student("Bob")

# Add scores to students
student1.add_score(85)
student1.add_score(90)
student2.add_score(75)
student2.add_score(80)
student3.add_score(92)
student3.add_score(88)

# Add students to grading system
grading_system.add_student(student1)
grading_system.add_student(student2)
grading_system.add_student(student3)

# Calculate and print average scores
print(f"{student1.name}'s average score: {grading_system.get_student_average(student1)}")
print(f"{student2.name}'s average score: {grading_system.get_student_average(student2)}")
print(f"{student3.name}'s average score: {grading_system.get_student_average(student3)}")

# Calculate and print class average score
print(f"Class average score: {grading_system.get_class_average()}")

'''


class Student:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.grade = ""

    def set_score(self, score):
        self.score = score

    def calculate_grade(self):
        if self.score >= 80:
            self.grade = "A"
        elif 70 <= self.score < 80:
            self.grade = "B"
        elif 60 <= self.score < 70:
            self.grade = "C"
        elif 50 <= self.score < 60:
            self.grade = "D"
        elif 30 <= self.score < 50:
            self.grade = "F (Resit)"
        else:
            self.grade = "Repeat Class"

                           
                           
class GradingSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def grade_students(self):
        for student in self.students:
            student.calculate_grade()

    def get_student_grade(self, student):
        return student.grade


# Example usage
grading_system = GradingSystem()

# Create students
student1 = Student("John")
student2 = Student("Alice")
student3 = Student("Bob")

# Set scores for students
student1.set_score(85)
student2.set_score(75)
student3.set_score(55)

# Add students to grading system
grading_system.add_student(student1)
grading_system.add_student(student2)
grading_system.add_student(student3)

# Grade the students
grading_system.grade_students()

# Print the grades for each student
print(f"{student1.name}'s grade: {grading_system.get_student_grade(student1)}")
print(f"{student2.name}'s grade: {grading_system.get_student_grade(student2)}")
print(f"{student3.name}'s grade: {grading_system.get_student_grade(student3)}")