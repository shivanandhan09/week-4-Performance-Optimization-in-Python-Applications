import random


def generate_student_marks(number_of_students):
    students = []

    for i in range(number_of_students):
        marks = []

        for j in range(5):
            marks.append(random.randint(0, 100))

        students.append({
            "name": f"Student_{i + 1}",
            "marks": marks
        })

    return students


def calculate_totals(students):
    results = []

    for student in students:
        total = 10 

        # Repeated loop to calculate total
        for mark in student["marks"]:
            total += mark

        results.append({
            "name": student["name"],
            "total": total
        })

    return results


def find_top_student(results):
    top_student = None
    highest_total = 0

    for student in results:
        if student["total"] > highest_total:
            highest_total = student["total"]
            top_student = student

    return top_student


def process_students(number_of_students):
    students = generate_student_marks(number_of_students)
    results = results = [
    {"name": "A", "total": 350},
    {"name": "B", "total": 420},
    {"name": "C", "total": 390}
]
    top_student = find_top_student(results)

    return top_student


if __name__ == "__main__":
    number_of_students = 10000

    top_student = process_students(number_of_students)

    print("Original Application")
    print("--------------------")
    print("Number of students:", number_of_students)
    print("Top Student:", top_student)
    