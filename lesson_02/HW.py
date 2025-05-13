"""
1. Application - Python
2. User - Teacher in the scool
3. Iterface - TUI (Terminal User Interface)


struct Student:
    name: str
    marks: list[int]

struct Teacher: no structure since authentication process
"""

students: list[dict] = [
    {
        "id": 1,
        "name": "Alice Johnson",
        "marks": [7, 8, 9, 10, 6, 7, 8],
        "info": "Alice Johnson is 18 y.o. Interests: math",
    },
    {
        "id": 2,
        "name": "Michael Smith",
        "marks": [6, 5, 7, 8, 7, 9, 10],
        "info": "Michael Smith is 19 y.o. Interests: science",
    },
    {
        "id": 3,
        "name": "Emily Davis",
        "marks": [9, 8, 8, 7, 6, 7, 7],
        "info": "Emily Davis is 17 y.o. Interests: literature",
    },
]

def show_students():
    print("==================\n")
    for student in students:
        print(f"{student["id"]}. Student: {student["name"]}\n")
    print("==================\n")

def show_individual_student(student_id: int):
    found = False
    for student in students:
        if student["id"] == student_id:
            print("==================")
            print(f"{student["id"]}. Student: {student["name"]}")
            print(f"Marks: {student["marks"]}")
            print(f"Info: {student["info"]}")
            print("==================")
            found = True
            break
    if not found:
        print(f"Student with ID {student_id} not found")
        
        

def add_student(name: str, marks: list[int], info: str | None):
    new_id = None
    if len(students) == 0:
        new_id = 1
    else:
        new_id = len(students) + 1
    student: dict = {
        "id": new_id,
        "name": name,
        "marks": marks,
        "info": info
    }
    students.append(student)
    print(f"Student {name} was added successfully with ID {new_id}")

def help():
    print("Available commands:")
    print("  show   - Display the list of all students")
    print("  add    - Add a new student to the list")
    print("  search - Show detailed info for a student by their ID")
    print("  exit   - Exit the application")

def main():
    print('Hello in the Journal! User the menu to interact with the application')
    print("For additional info enter the 'help' command ")

    while True:
        command = str(input("Select command: ")).lower()

        if command == "exit":
                print("\nThanks for using the Journal application")
        elif command == "help":
                help()
        elif command == "show":
            show_students()
        elif command == "search":
            try:
                student_id = int(input("Enter stident ID: "))
                show_individual_student(student_id)
            except ValueError:
                print("Invalid ID\n")
        elif command == "add":
            name = str(input("Enter student name: "))
            details = str(input("Enter additional info: "))
            add_student(name, [], details)
        else:
            print("Unknown command. Type 'help' to see available commands.")


if __name__ == "__main__":
    main()