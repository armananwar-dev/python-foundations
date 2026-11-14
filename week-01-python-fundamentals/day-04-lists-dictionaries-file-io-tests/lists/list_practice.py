
# ==========================================
# Student Marks Management
# Practice: Python Lists, Loops, and Methods
# ==========================================

# 1. Create a list of student marks
students = [45, 67, 79, 98, 90]

# 2. Initialize variables
total = 0

# 3. Display first and last marks
print("First mark:", students[0])
print("Last mark:", students[-1])

# 4. Add a new student's marks
students.append(85)

# 5. Update the second student's marks
students[1] = 95

# 6. Display all student marks and calculate total
print("\nAll Student Marks:")

for marks in students:
    print(marks)
    total += marks

# 7. Calculate average
average = total / len(students)

# 8. Display results
print("\n----- Results -----")
print("Total marks:", total)
print("Number of students:", len(students))
print("Average marks:", average)
