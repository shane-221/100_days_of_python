# Todo: creating a dictionary from a list
import random
names = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Isaac", "Julia"]
student_scores = { student: random.randint(0,100) for student in names}

# Todo: if condtion applied to the dictionary:
passed_students ={students: student_scores[students] for students in student_scores if student_scores[students]>50}