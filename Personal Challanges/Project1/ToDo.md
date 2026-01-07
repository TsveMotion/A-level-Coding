# ToDo – Student Results & Grade System (A-Level Python)

This file outlines planned improvements, extensions, and evaluation points
for the console-based Student Results and Grade System written in Python.

The program calculates averages, assigns grades, stores student records,
and allows searching by student name.

---

## ✅ Completed
- [x] Input number of students
- [x] Input student name and three test scores
- [x] Calculate average score for each student
- [x] Assign grades (A–F) using selection
- [x] Store student data using a list of dictionaries
- [x] Display a formatted summary of all students
- [x] Search for a student by name
- [x] Display student results if found
- [x] Handle case where student is not found

---

## 🔧 Improvements (Next Steps)

### Code Structure
- [ ] Move grade calculation into a separate function
- [ ] Move average calculation into a function
- [ ] Move student search into a reusable function (already partially complete)
- [ ] Separate input, processing, and output into clear sections
- [ ] Improve variable naming consistency

---

### Input Validation
- [ ] Ensure student name is not empty
- [ ] Ensure test scores are between 0 and 100
- [ ] Handle non-integer input for test scores
- [ ] Prevent negative scores
- [ ] Prevent duplicate student names

---

### Searching & Analysis
- [ ] Make search case-insensitive
- [ ] Allow repeated searches without restarting the program
- [ ] Display all test scores when a student is found
- [ ] Add option to search for highest or lowest scoring student

---

### Statistics & Reporting
- [ ] Calculate and display class average
- [ ] Display highest and lowest student averages
- [ ] Count number of students in each grade band
- [ ] Sort students by average score (highest first)
- [ ] Sort students alphabetically by name

---

## 🚀 A-Level Extension (Grade 8–9)
- [ ] Save student data to a text or CSV file
- [ ] Load student data from a file
- [ ] Add a simple menu system (add/search/summary/exit)
- [ ] Refactor program to avoid global variables
- [ ] Store students in a dictionary keyed by name
- [ ] Add comments explaining design decisions

---

## 🧠 Evaluation & Design
- [ ] Justify the use of a list of dictionaries
- [ ] Compare using a list vs a dictionary for storing students
- [ ] Evaluate the use of local variables instead of global variables
- [ ] Explain how the program could scale for larger classes
- [ ] Identify potential sources of bugs and how they are avoided

---

## 📌 Notes
This program is fully console-based and uses no external libraries.
It is designed to reflect **OCR A-Level Computer Science exam-style programming**
and structured problem-solving techniques.

---
