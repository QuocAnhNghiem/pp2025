
students = []
courses = []
marks = {}

def input_number_of_students():
    count = int(input("Enter number of students in class: "))
    return count

def input_student_information():
    print("--- Input Student Information ---")
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    dob = input("Enter Date of Birth (DoB): ")
    
    student = {'id': sid, 'name': name, 'dob': dob}
    students.append(student)

def input_number_of_courses():
    count = int(input("Enter number of courses: "))
    return count

def input_course_information():
    print("--- Input Course Information ---")
    cid = input("Enter Course ID: ")
    name = input("Enter Course Name: ")
    
    course = {'id': cid, 'name': name}
    courses.append(course)

def input_marks():
    print("--- Input Marks ---")
    list_courses()
    
    course_id = input("Select Course ID to input marks: ")
    
    if course_id not in [c['id'] for c in courses]:
        print("Course not found!")
        return

    if course_id not in marks:
        marks[course_id] = {}

    for s in students:
        mark = float(input(f"Enter mark for student {s['name']} (ID: {s['id']}): "))
        marks[course_id][s['id']] = mark

def list_students():
    print("\n-------------------------")
    print("LIST OF STUDENTS:")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}")
    print("-------------------------\n")

def list_courses():
    print("\n-------------------------")
    print("LIST OF COURSES:")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")
    print("-------------------------\n")

def show_student_marks():
    print("--- Show Marks ---")
    list_courses()
    course_id = input("Select Course ID to view marks: ")
    
    if course_id in marks:
        print(f"\nMarks for Course {course_id}:")
        for s in students:
            m = marks[course_id].get(s['id'], "N/A") 
            print(f"Student: {s['name']}, Mark: {m}")
    else:
        print("No marks data for this course yet.")

if __name__ == "__main__":
    num_students = input_number_of_students()
    for _ in range(num_students):
        input_student_information()

    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        input_course_information()

    while True:
        print("\n--- MENU ---")
        print("1. List Students")
        print("2. List Courses")
        print("3. Input Marks")
        print("4. Show Marks")
        print("5. Exit")
        choice = input("Your choice: ")

        if choice == '1':
            list_students()
        elif choice == '2':
            list_courses()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            show_student_marks()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")