number_books_loaned = int(input("How many books have you loaned?"))
total_loans = []



for i in range(number_books_loaned):
    book_name = input("What is the name of the book?")
    student_name = input("What is the name of the student?")
    number_days_borrowed = int(input("How many days have you borrowed the book?"))

    if number_days_borrowed > 14:
        due_status = "Overdue"
    elif number_days_borrowed <= 14:
        due_status = "On Time"

    # Creating the dictionary here
    loans = {
        "book_name": book_name,
        "student_name": student_name,
        "number_days_borrowed": number_days_borrowed,
        "due_status": due_status
    }
    total_loans.append(loans)

print(total_loans)

print("------SUMMARY------")
print(f"Number of books loaned: {number_books_loaned}")

for loans in total_loans:
    print(f"Student Name: {loans['student_name']} # Book Name: {loans['book_name']} # Days Borrowed: {loans['number_days_borrowed']} # Due Status: {loans['due_status']}")
    