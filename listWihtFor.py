students = [
    {"name": "Ron", "house": "Gryffindor", "pet": "Stag"},
    {"name": "Harry", "house": "Gryffindor", "pet": "Outter"},
    {"name": "Hermione", "house": "Gryffindor", "pet": "Bee"},
    {"name": "Draco", "house": "Slytherin", "pet": None},
]

for student in students:
    print(students.index(student) + 1 ,student["name"], student["pet"], sep= ", ")

for i in range(len(students)):
    print((i + 1), students[i]["name"], students[i]["house"], sep=", ")