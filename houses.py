students= [
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"ron", "house":"Gryffindor"},
    {"name":"Draco", "house":"slytherin"},
    {"name":"padma", "house":"Ravencklaw"}
]

houses= set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)

