class Student:
    def __init__(self, name, number, city, average_grade):
        self.name = name
        self.number = number
        self.city = city
        self.average_grade = average_grade

    def __str__(self):
        return f"Name: {self.name}, Number: {self.number}, City: {self.city}, Average Grade: {self.average_grade}"

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(student)

    def search_student(self, number):
        for student in self.students:
            if student.number == number:
                return student
        return None

    def delete_student(self, number):
        for student in self.students:
            if student.number == number:
                self.students.remove(student)
                return f"Student with number {number} deleted successfully."
        return f"Student with number {number} not found."

sms = StudentManager()
sms.add_student(Student("John Doe", 1001, "Veliko Tarnovo", 5))
sms.add_student(Student("Mark", 1003, "Sofia", 3))
print("All students:")
sms.display_students()

number_to_search = 1001
found_student = sms.search_student(number_to_search)
if found_student:
    print(f"Student with number {number_to_search} found: {found_student}")
else:
    print(f"Student with number {number_to_search} not found!")

number_to_delete = 1001
print(sms.delete_student(number_to_delete))
print("Remaining students: ")
sms.display_students()