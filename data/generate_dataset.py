import json
import random

names = [
    "Rahul Sharma", "Anjali Verma", "Amit Singh", "Priya Patel",
    "Rohit Kumar", "Sneha Gupta", "Arjun Yadav", "Neha Joshi",
    "Vikas Mishra", "Pooja Singh"
]

subjects = ["Math", "Science", "English", "Computer", "Social Science"]

def get_performance(avg):
    if avg >= 85:
        return "Excellent"
    elif avg >= 70:
        return "Good"
    elif avg >= 50:
        return "Average"
    else:
        return "Poor"

students = []

for i in range(1, 201):
    marks = {sub: random.randint(40, 100) for sub in subjects}
    avg = round(sum(marks.values()) / len(subjects), 2)

    weak_subjects = [sub for sub, m in marks.items() if m < 60]

    student = {
        "student_id": f"S{i:03}",
        "name": random.choice(names),
        "class": str(random.randint(8, 12)),
        "section": random.choice(["A", "B", "C"]),
        "attendance_percentage": random.randint(60, 100),
        "marks": marks,
        "average_marks": avg,
        "performance": get_performance(avg),
        "weak_subjects": weak_subjects,
        "remarks": "Needs improvement" if avg < 60 else "Doing well"
    }

    students.append(student)

with open("students.json", "w") as f:
    json.dump(students, f, indent=4)

print("✅ Dataset generated successfully!")