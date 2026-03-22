import json
from langchain_core.documents import Document

def load_students(file_path: str):
    with open(file_path, "r") as f:
        data = json.load(f)

    documents = []

    for student in data:
        content = f"""
        Student ID: {student['student_id']}
        Name: {student['name']}
        Class: {student['class']}
        Section: {student['section']}
        Attendance: {student['attendance_percentage']}%
        
        Marks:
        Math: {student['marks']['Math']}
        Science: {student['marks']['Science']}
        English: {student['marks']['English']}
        Computer: {student['marks']['Computer']}
        Social Science: {student['marks']['Social Science']}
        
        Average Marks: {student['average_marks']}
        Performance: {student['performance']}
        Weak Subjects: {", ".join(student['weak_subjects'])}
        Remarks: {student['remarks']}
        """

        metadata = {
            "student_id": student["student_id"],
            "class": student["class"],
            "performance": student["performance"]
        }

        documents.append(Document(page_content=content, metadata=metadata))

    return documents

# if __name__ == "__main__":
#     documents = load_students("C:/Users/asus/Downloads/ANUJ_Student_Perfromance_RAG_Project/data/students.json")
#     for doc in documents:
#         print(doc.page_content)
#         print(doc.metadata)
#         print("\n---\n")