number_students = int(input("For how many students would you like to input data for? "))

students = []


for i in range(number_students):
    student_name = input("What is the name of student? ")
    student_test_1 = int(input("What is the score for test 1? "))
    student_test_2 = int(input("What is the score for test 2? "))
    student_test_3 = int(input("What is the score for test 3? "))
    average = (student_test_1 + student_test_2 + student_test_3) / 3

    grade = ""
    if average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    student = {
        "name": student_name,
        "test_1": student_test_1,
        "test_2": student_test_2,
        "test_3": student_test_3,
        "average_mark": average,
        "grade": grade
    }
    students.append(student)



print("---------SUMAMRY---------")
for student in students:
    print(f"Name: {student['name']} | Average: {student['average_mark']:.1f} | Grade: {student['grade']}")


def search_student(search_name):
    for student in students:
        if student['name'] == search_name:
            return student
    return None

Seach_Student = input("What student would you like to search for? ")
result = search_student(Seach_Student)

if result is not None:
    print(f"Name: {result['name']} | Average: {result['average_mark']:.1f} | Grade: {result['grade']}")
else:
    print("Student not found")