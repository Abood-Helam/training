students = [
    {"name":"Hermeone", "house":"Gryffindor"},
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"Ron", "house":"Gryffindor"},
    {"name":"Draco", "house":"slytherin"},
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])

gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])


students = ["Hermione", "Harry", "Ron"]

gryffindors = []

for student in students:
    gryffindors.append({"name":student, "house":"Gryffindor"})

print(gryffindors)

students = ["Hermione", "Harry", "Ron"]

gryffindors = [{"name":student, "house":"Gryffindor"} for student in students]

print(gryffindors)

students = ["Hermione", "Harry", "Ron"]

gryffindors = {student:"Gryffindor" for student in students}

print(gryffindors)

students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)