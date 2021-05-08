class Students:
    def __init__(self, student_id, student_name, student_dob):
        self.student_id = sid
        self.student_name = sname
        self.student_dob = dob

    def set_student_id(self, sid):
        self.student_id = sid

    def get_student_id(self):
        return self.student_id

    def set_student_name(self, sname):
        self.student_name = sname

    def get_student_name(self):
        return self.student_name

    def set_student_dob(self, dob):
        self.student_dob = dob

    def get_student_dob(self):
        return self.student_dob

    def ShowStudentInfo(self):
        print("Student ID : " + self.student_id)
        print("Student name : " + self.student_name)
        print("Date of birth : " + self.student_dob)
        print(" \n ")
        
class Courses:
    def __init__(self, course_id, course_name):
        self.course_id = cid
        self.course_name = cname

    def set_course_id(self, cid):
        self.course_id = cid

    def get_course_id(self):
        return self.course_id

    def set_course_name(self, cname):
        self.course_name = cname

    def get_course_name(self):
        return self.course_name

    def ShowCourse(self):
        print("Course Id : " + self.course_id)
        print("Course name : " + self.name)
        print(" \n ")

class Marks:
    def __init__(self, student_id, course_id, mark):
        self.student_id = sid
        self.course_id = cid
        self.mark = mark

    def set_student_id(self, sid):
        self.student_id = sid
    
    def get_student_id(self):
        return self.student_id

    def set_course_id(self, cid):
        self.course_id = cid

    def get_course_id(self):
        return self.course_id

    def set_mark(self, mark):
        self.mark = mark

    def get_mark(self):
        return self.mark

    def ShowMark(self):
        


def NumberOfStudent():
    student_number = int(input("Please enter the number of students in the class: "))
    return student_number

def StudentInfo(): 
    student_id = input("Enter Student ID: \n")
    student_name = input("Enter Student name: \n")
    student_dob = input("Enter Student date of birth: \n")
    return student_id, student_name, student_dob

def NumberOfCourse():
    course_number = int(input("Please enter the number of courses: \n"))
    return course_number

def CourseInfo():
    course_id = input("Enter course id: \n")
    course_name = input("Enter course name: \n")
    return course_id, course_name

def CourseMark():
    for i in range(len(students)):
        mark = float(input("Enter student " + f"{student_name}" + " marks \n"))
# students[i].get("name")        
        marks[i].update({course: mark})

def ListCourses(courses):
    print("- Course information - \n")
    # for k, v in courses.items():
    #     print(k, v)
    for i in range(len(courses)):
        print(f"{course_id} \n {course_name}")
        print("\n")

def ListStudents(students):
    print("- Student information - \n")
    for i in range(len(students)):
        print(f"{student_id} \n {student_name} \n {student_dob}")
        print("\n")

def ListMarks(marks):
    print("- Course marks - \n")
    for i in range(len(students)):
            print(f"{student_name}" + " mark:")
            print(marks[i].get(select_course))
            print("\n")


if __name__ == "__main__":
    print("~Student mark management system~ \n")
    student_number = NumberOfStudent()
    # if student_number == 0:
    # print("Please input valid number of student \n")
    if student_number == 1:
        print("Please input student information: \n")
    else:
    # if student_number > 1:
        print(f"Please input {student_number} students information in sequence: \n")
    # else:
    #     break
    for i in range(0, student_number):
        print(f"Student {i+1} information:")
        student_id, student_name, student_dob = StudentInfo()
        students.append({"id": student_id, "name": student_name, "dob": student_dob})
        print(f"{student_name} information has been added \n" )
    
    course_number = NumberOfCourse()
    print("Please input courses information: \n")
    for i in range(0, course_number):
        course_id, course_name = CourseInfo()
        courses.append({"id": course_id, "name": course_name})

    action1 = input("To continue please press 1, otherwise to stop please press 2 \n")
    while (action1 == "1"):
        action2 = input("Please press 1 to start inputting marks for courses, otherise press any other key to skip \n ")
        if (action2 == "1"):
            select_course_id = input("Enter ID of the course you want to input marks: ")
            for i in range(len(courses)):
                if courses[i].get("id") == select_course_id:
                    print(f"{course_name}" + " has been selected. \n")
                    CourseMark()
                else:
                    print("No valid courses. \n")
                    break
        else:
            break
    action3 = input("Press 1 if you want to continue: \n")
    while (action3 == "1"):
        action4 = input("Press 1 to view student list." + "\n" + "Press 2 to view courses and marks. \n")
        if (action4 == "1"):
            ListStudents(students)
        else:
            if(action4 == "2"):
                ListCourses(courses)
                ListMarks(marks)
            else:
                break
    action5 = input("Press 1 to exit. \n")
    if (action5 == "1"):
        exit()

