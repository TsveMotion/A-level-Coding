# 🔥 Challenge 1: Smart Timetable Optimiser (A* Level)
**OCR A-Level Computer Science**

---

## 📌 Problem Statement (Exam Style)
A school wants a program to generate a weekly timetable for multiple student groups.

Each lesson must be placed into a valid time slot while meeting these constraints:
- A teacher cannot teach two lessons at the same time.
- A student group cannot have two lessons at the same time.
- Some subjects require a **double period** (two consecutive time slots).
- The timetable should be *as good as possible*, aiming to **minimise teacher gaps** (idle periods).

The program must:
- Produce a timetable if possible, or
- Clearly explain why it is impossible (which constraint failed).

---

## ✅ Phase 1: Understand the Problem
- [ ] Read the full problem and identify **inputs**, **outputs**, and **constraints**
- [ ] List all entities involved:
  - [ ] Subjects
  - [ ] Teachers
  - [ ] Student groups
  - [ ] Time slots
- [ ] Clarify what a **double period** means in terms of time slots

---

## 🧱 Phase 2: Design the Data Structures
- [ ] Decide how to represent time slots (e.g. tuples, strings, indexes)
- [ ] Choose a structure for teachers and their subjects
  - [ ] Dictionary: `teacher → list of subjects`
- [ ] Choose a structure for the timetable
  - [ ] 2D array or dictionary: `(group, time_slot) → subject`
- [ ] Decide how to track:
  - [ ] Teacher availability
  - [ ] Student group availability

---

## 🗺 Phase 3: Model as a Graph / Constraint Problem
- [ ] Identify **nodes** (e.g. lessons to schedule)
- [ ] Identify **edges / constraints**:
  - [ ] Teacher clashes
  - [ ] Student group clashes
  - [ ] Double period adjacency
- [ ] Decide where a **greedy choice** can be applied
  - [ ] Least available teacher first
  - [ ] Subjects with double periods first

---

## ⚙️ Phase 4: Core Algorithm (Greedy Scheduler)
- [ ] Sort subjects by difficulty of placement
- [ ] For each subject:
  - [ ] Try to assign a valid time slot
  - [ ] Check teacher availability
  - [ ] Check student group availability
  - [ ] Check double-period requirement
- [ ] If valid:
  - [ ] Place subject in timetable
  - [ ] Update availability records
- [ ] If invalid:
  - [ ] Try next best slot

---

## 🚫 Phase 5: Failure Detection (A* Twist)
- [ ] Detect when no valid slot exists
- [ ] Identify **which constraint failed**:
  - [ ] Teacher conflict
  - [ ] Student group conflict
  - [ ] Double period impossible
- [ ] Output a clear error message explaining the failure

---

## 📉 Phase 6: Optimisation (Minimise Teacher Gaps)
- [ ] Track each teacher’s daily schedule
- [ ] Calculate gaps between lessons
- [ ] Prefer placements that:
  - [ ] Reduce idle periods
  - [ ] Cluster lessons together
- [ ] Justify why this improves timetable quality

---

## 📊 Phase 7: Efficiency Analysis (Required for A*)
- [ ] Identify main loops
- [ ] Calculate time complexity (Big-O)
- [ ] Identify worst-case scenario
- [ ] Explain how constraints affect performance
- [ ] Suggest one possible optimisation

---

## 🧪 Phase 8: Testing
- [ ] Test with:
  - [ ] Minimal data
  - [ ] Fully packed timetable
  - [ ] Impossible timetable
- [ ] Verify constraints are never broken
- [ ] Confirm correct failure messages

---

## ✍️ Phase 9: Evaluation (Exam Gold)
- [ ] Explain why global variables were avoided/used
- [ ] Justify greedy approach
- [ ] Discuss limitations of the solution
- [ ] Suggest an alternative (e.g. backtracking)

---

## 🏁 Final Check
- [ ] Code is readable and commented
- [ ] Variable names are meaningful
- [ ] Algorithm is explained clearly
- [ ] Ready to describe in OCR exam conditions

---

🔥 **If you can complete every checkbox and explain each decision, this is A\***  
No shortcuts. This is real Computer Science.
