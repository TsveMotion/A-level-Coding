# ToDo – Library Book Loan System (A-Level Python)

This file outlines planned improvements and extensions for the console-based
Library Book Loan System written in Python.

The aim is to improve structure, reliability, and functionality while staying
within **OCR A-Level Computer Science** expectations.

---

## ✅ Completed
- [x] Accept number of book loans
- [x] Input book name, student name, and days borrowed
- [x] Store loan records using a list of dictionaries
- [x] Determine due status (On Time / Overdue)
- [x] Display a formatted summary of all loans
- [x] Output total number of books loaned

---

## 🔧 Improvements (Next Steps)

### Code Structure
- [ ] Move loan creation into a function
- [ ] Move summary printing into a separate function
- [ ] Remove unnecessary `elif` and use `else` where appropriate
- [ ] Improve variable naming consistency

---

### Input Validation
- [ ] Prevent empty book or student names
- [ ] Ensure number of days borrowed is between 1 and 30
- [ ] Handle non-integer input for days borrowed
- [ ] Prevent duplicate book titles

---

### Searching & Analysis
- [ ] Add search by book title (case-insensitive)
- [ ] Display borrower and due status when searched
- [ ] Count and display number of overdue books
- [ ] Display longest and shortest loan durations

---

### Sorting & Reporting
- [ ] Sort loans by days borrowed (highest first)
- [ ] Sort loans alphabetically by book name
- [ ] Output a clearer report using formatted strings
- [ ] Separate summary output from data input phase

---

## 🚀 A-Level Extension (Grade 8–9)
- [ ] Save loan data to a text or CSV file
- [ ] Load loan data from a file
- [ ] Allow updating or returning books
- [ ] Introduce basic menu system (add/search/summary/exit)
- [ ] Refactor program to avoid global variables
- [ ] Add comments explaining design decisions

---

## 🧠 Evaluation
- [ ] Justify choice of list of dictionaries
- [ ] Compare this approach to using a dictionary keyed by book name
- [ ] Explain how the program could scale for a larger library
- [ ] Identify potential issues if global variables were used

---

## 📌 Notes
This project is console-based and does not use any external libraries.
It is designed to reflect **exam-style programming tasks** and structured
problem-solving techniques required for OCR A-Level Computer Science.

---
