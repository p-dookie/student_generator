from math import floor
import names
import uuid
import random
import json

course_selection = ["science", "math", "social_studies", "english", "french", "writing", "woodwork", "metalwork",
                    "car_mech", "engineering", "fire_prevention", "hair_dressing"]

students = []


def create_student(num) -> object:
    for i in range(num):
        name = names.get_full_name()
        _id = f"{uuid.uuid1()}"
        courses = []
        for f in range(8):
            while True:
                course = floor(random.random() * len(course_selection))
                if course_selection[course] not in courses:
                    courses.append(course_selection[course])
                    break
        student_prime = {"name": name, "_id": _id, "courses": courses}
        students.append(student_prime)
        print(i)

    with open('stored_sample_data.json', 'w') as outfile:
        json.dump(students, outfile)

    return students

print(create_student(10))
