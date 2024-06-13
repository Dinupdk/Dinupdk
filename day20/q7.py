#Question: Given the dictionary student_grades, find the highest grade and its corresponding student name.
#  The dictionary contains student names as keys and their grades as values.
#Expected Input: student_grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
#Expected Output: ("Bob", 90)
def get_highest_grade(student_grades):
    # Find the student with the highest grade using the max function
    highest_grade_student = max(student_grades, key=student_grades.get)
    # Get the highest grade
    highest_grade = student_grades[highest_grade_student]
    # Return the student name and the highest grade
    return (highest_grade_student, highest_grade)

# Example usage
student_grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
result = get_highest_grade(student_grades)
print(result)
