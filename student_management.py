# Student Management System

students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter age: ")
        course = input("Enter course: ")

        student = {
            "Name": name,
            "Age": age,
            "Course": course
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        print("\nStudent List")
        for s in students:
            print(s)

    elif choice == "3":
        print("Program closed")
        break

    else:
        print("Invalid choice")