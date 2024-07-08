import random

def generate_marks(num_students, min_mark=0.0, max_mark=100.0):
    marks = {}
    for i in range(1, num_students + 1):
        marks[f"Student_{i}"] = round(random.uniform(min_mark, max_mark), 2)
    return marks

# Example usage
num_students = 10  # Number of students
marks = generate_marks(num_students)

# Display the generated marks
for student, mark in marks.items():
    print(f"{student}: {mark}")
