# -Student-Management-System
import json
import os

FILE_NAME = "students.json"


# ---------------- File Handling ----------------
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# ---------------- Student Operations ----------------
def add_student(students):
    roll_no = input("Enter Roll Number: ")

    # Check for duplicate roll number
    for student in students:
        if student["roll_no"] == roll_no:
            print("❌ Student with this Roll Number already exists.")
            return

    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    students.append({
        "roll_no": roll_no,
        "name": name,
        "marks": marks
    })

    save_students(students)
    print("✅ Student added successfully!")


def update_student(students):
    roll_no = input("Enter Roll Number to update: ")

    for student in students:
        if student["roll_no"] == roll_no:
            student["name"] = input("Enter New Name: ")
            student["marks"] = input("Enter New Marks: ")
            save_students(students)
            print("✅ Student updated successfully!")
            return

    print("❌ Student not found.")


def delete_student(students):
    roll_no = input("Enter Roll Number to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            save_students(students)
            print("✅ Student deleted successfully!")
            return

    print("❌ Student not found.")


def search_student(students):
    roll_no = input("Enter Roll Number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found:")
            print(f"Roll No : {student['roll_no']}")
            print(f"Name    : {student['name']}")
            print(f"Marks   : {student['marks']}")
            return

    print("❌ Student not found.")


def display_students(students):
    if not students:
        print("⚠️ No student records found.")
        return

    print("\n" + "-" * 50)
    print(f"{'Roll No':<15}{'Name':<20}{'Marks':<10}")
    print("-" * 50)

    for student in students:
        print(f"{student['roll_no']:<15}{student['name']:<20}{student['marks']:<10}")

    print("-" * 50)


# ---------------- Main Menu ----------------
def main():
    students = load_students()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Display All Students")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            update_student(students)
        elif choice == "3":
            delete_student(students)
        elif choice == "4":
            search_student(students)
        elif choice == "5":
            display_students(students)
        elif choice == "6":
            print("👋 Exiting program. bye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
