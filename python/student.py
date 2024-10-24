class Student:
    students = []  

    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def add_student(self):
        #if exists
        for student in Student.students:
            if student['student_id'] == self.student_id:
                print("Student ID already exists.")
                return
        # Adding student details to the list
        Student.students.append({
            'student_id': self.student_id,
            'name': self.name,
            'age': self.age,
            'grade': self.grade
        })
        print("Student added successfully.")


    def display_student(student_id):
        for student in Student.students:
            if student['student_id'] == student_id:
                print(f"ID: {student['student_id']}")
                print(f"Name: {student['name']}")
                print(f"Age: {student['age']}")
                print(f"Grade: {student['grade']}")
                return
        print("Student not found.")

   
    def search_student(student_id):
        for student in Student.students:
            if student['student_id'] == student_id:
                return student
        return None

  
    def delete_student(student_id):
        for student in Student.students:
            if student['student_id'] == student_id:
                Student.students.remove(student)
                print("Student deleted successfully.")
                return
        print("Student not found.")

    
    def update_student(student_id, name=None, age=None, grade=None):
        for student in Student.students:
            if student['student_id'] == student_id:
                if name:
                    student['name'] = name
                if age is not None:
                    student['age'] = age
                if grade:
                    student['grade'] = grade
                print("Student details updated successfully.")
                return
        print("Student not found.")

def menu():
    while True:
        print("\nStudent Management System")
        print("1. Accept Student Details")
        print("2. Display Student Details")
        print("3. Search Details of a Student")
        print("4. Delete Details of a Student")
        print("5. Update Student Details")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            age = int(input("Enter Student Age: "))
            grade = input("Enter Student Grade: ")
            student = Student(student_id, name, age, grade)
            student.add_student()

        elif choice == '2':
            student_id = input("Enter Student ID to Display: ")
            Student.display_student(student_id)

        elif choice == '3':
            student_id = input("Enter Student ID to Search: ")
            student = Student.search_student(student_id)
            if student:
                print(f"ID: {student['student_id']}")
                print(f"Name: {student['name']}")
                print(f"Age: {student['age']}")
                print(f"Grade: {student['grade']}")
            else:
                print("Student not found.")

        elif choice == '4':
            student_id = input("Enter Student ID to Delete: ")
            Student.delete_student(student_id)

        elif choice == '5':
            student_id = input("Enter Student ID to Update: ")
            name = input("Enter new Student Name (or press Enter to skip): ")
            age_input = input("Enter new Student Age (or press Enter to skip): ")
            age = int(age_input) if age_input else None
            grade = input("Enter new Student Grade (or press Enter to skip): ")
            Student.update_student(student_id, name or None, age, grade or None)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

menu()

