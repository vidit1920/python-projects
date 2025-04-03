import csv

FILE_NAME = "students.csv"

def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'

def add_student():
    students = []
    for _ in range(10):
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")
        marks = [int(input(f"Enter marks for Subject {_+1}: ")) for _ in range(5)]
        total_marks = sum(marks)
        percentage = total_marks / 5
        grade = calculate_grade(percentage)
        students.append([student_id, name, age, course, *marks, total_marks, percentage, grade])
    
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students)
    print("Records added successfully!")

def display_students():
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No records found.")

def search_student(student_id):
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == student_id:
                print("Record Found:", row)
                return
    print("Student not found.")

def update_marks(student_id):
    students = []
    found = False
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == student_id:
                new_marks = [int(input(f"Enter new marks for Subject {_+1}: ")) for _ in range(5)]
                total_marks = sum(new_marks)
                percentage = total_marks / 5
                grade = calculate_grade(percentage)
                row = [student_id, row[1], row[2], row[3], *new_marks, total_marks, percentage, grade]
                found = True
            students.append(row)
    
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students)
    
    if found:
        print("Marks updated successfully!")
    else:
        print("Student not found.")

def delete_student(student_id):
    students = []
    found = False
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != student_id:
                students.append(row)
            else:
                found = True
    
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students)
    
    if found:
        print("Student record deleted successfully!")
    else:
        print("Student not found.")

def top_3_students():
    students = []
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        students = [row for row in reader]
    
    students.sort(key=lambda x: float(x[-2]), reverse=True)
    print("Top 3 Students:")
    for student in students[:3]:
        print(student)

def main():
    while True:
        print("\n1. Add New Student Records")
        print("2. Display All Student Records")
        print("3. Search Student by ID")
        print("4. Update Student Marks")
        print("5. Delete Student Record")
        print("6. Generate Top 3 Students Report")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            student_id = input("Enter Student ID: ")
            search_student(student_id)
        elif choice == '4':
            student_id = input("Enter Student ID: ")
            update_marks(student_id)
        elif choice == '5':
            student_id = input("Enter Student ID: ")
            delete_student(student_id)
        elif choice == '6':
            top_3_students()
        elif choice == '7':
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
