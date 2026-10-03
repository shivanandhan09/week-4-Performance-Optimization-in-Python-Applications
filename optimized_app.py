import random


def generate_student_marks(number_of_students):
    students = []

    for i in range(number_of_students):
        marks = [random.randint(0, 100) for _ in range(5)]

        students.append({
            "name": f"Student_{i + 1}",
            "marks": marks
        })

    return students


def calculate_totals(students):
    results = []

    for student in students:
        total = sum(student["marks"])

        results.append({
            "name": student["name"],
            "total": total
        })

    return results


def find_top_student(results):
    return max(results, key=lambda student: student["total"])


def process_students(number_of_students):
    students = generate_student_marks(number_of_students)
    results = calculate_totals(students)
    top_student = find_top_student(results)

    return top_student


if __name__ == "__main__":
    number_of_students = 10000

    top_student = process_students(number_of_students)

    print("Optimized Application")
    print("---------------------")
    print("Number of students:", number_of_students)
    print("Top Student:", top_student)