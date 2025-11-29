
students = [] # List of dictionaries: Lưu danh sách sinh viên
courses = []  # List of dictionaries: Lưu danh sách môn học
marks = {}    # Dictionary: Lưu điểm. Cấu trúc: {course_id: {student_id: mark}}

# 1. Các hàm nhập liệu (Input functions) [cite: 145]

def input_number_of_students():
    # Nhập số lượng sinh viên [cite: 146]
    count = int(input("Enter number of students in class: "))
    return count

def input_student_information():
    # Nhập thông tin sinh viên: id, name, DoB [cite: 147]
    print("--- Input Student Information ---")
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    dob = input("Enter Date of Birth (DoB): ")
    
    # Lưu vào dictionary, rồi thêm vào list students
    student = {'id': sid, 'name': name, 'dob': dob}
    students.append(student)

def input_number_of_courses():
    # Nhập số lượng môn học [cite: 148]
    count = int(input("Enter number of courses: "))
    return count

def input_course_information():
    # Nhập thông tin môn học: id, name [cite: 149]
    print("--- Input Course Information ---")
    cid = input("Enter Course ID: ")
    name = input("Enter Course Name: ")
    
    # Lưu vào dictionary, rồi thêm vào list courses
    course = {'id': cid, 'name': name}
    courses.append(course)

def input_marks():
    # Chọn môn học và nhập điểm cho sinh viên [cite: 150]
    print("--- Input Marks ---")
    list_courses() # Hiển thị danh sách môn để chọn
    
    course_id = input("Select Course ID to input marks: ")
    
    # Kiểm tra xem môn học có tồn tại không
    if course_id not in [c['id'] for c in courses]:
        print("Course not found!")
        return

    # Khởi tạo dictionary điểm cho môn này nếu chưa có
    if course_id not in marks:
        marks[course_id] = {}

    # Duyệt qua danh sách sinh viên để nhập điểm
    for s in students:
        mark = float(input(f"Enter mark for student {s['name']} (ID: {s['id']}): "))
        # Lưu điểm vào dictionary marks
        marks[course_id][s['id']] = mark

# 2. Các hàm hiển thị (Listing functions) [cite: 151]

def list_students():
    # Liệt kê danh sách sinh viên [cite: 153]
    print("\n-------------------------")
    print("LIST OF STUDENTS:")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}")
    print("-------------------------\n")

def list_courses():
    # Liệt kê danh sách môn học [cite: 152]
    print("\n-------------------------")
    print("LIST OF COURSES:")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")
    print("-------------------------\n")

def show_student_marks():
    # Hiển thị điểm sinh viên cho một môn học cụ thể [cite: 155]
    print("--- Show Marks ---")
    list_courses()
    course_id = input("Select Course ID to view marks: ")
    
    if course_id in marks:
        print(f"\nMarks for Course {course_id}:")
        for s in students:
            # Lấy điểm từ dictionary marks, nếu không có thì để "N/A"
            m = marks[course_id].get(s['id'], "N/A") 
            print(f"Student: {s['name']}, Mark: {m}")
    else:
        print("No marks data for this course yet.")

# --- MAIN PROGRAM ---
# Đây là luồng chạy chính của chương trình
if __name__ == "__main__":
    # Nhập số lượng và thông tin sinh viên
    num_students = input_number_of_students()
    for _ in range(num_students):
        input_student_information()

    # Nhập số lượng và thông tin môn học
    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        input_course_information()

    # Menu đơn giản để chọn chức năng tiếp theo
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