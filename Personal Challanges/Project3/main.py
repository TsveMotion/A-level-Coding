number_student_groups = int(input("How many student groups do you have?"))

#=========================================================================

classifications = []


def classification():
    for i in range(number_student_groups):
        student_group = input("What is the name of student group " + str(i+1) + "?")
        teacher_name = input("What is the name of teacher " + str(i+1) + "?")
        subject = input("What is the name of subject " + str(i+1) + "?")

        classification = {
            "student_group": student_group,
            "teacher_name": teacher_name,
            "subject": subject
        }
        classifications.append(classification)


classification()


total_lessons_per_day = 5
total_days = 5
total_hours_per_week = total_days * total_lessons_per_day

for classifcation in classifications:
    print(f"Student Group: {classifcation['student_group']} | Teacher: {classifcation['teacher_name']}")
    lessons = ["","","","",""]
    for lesson_num in range(lessons):
        lessons = lessons[lesson_num]
        print(f"Lesson {lesson_num+1}: {lessons}")