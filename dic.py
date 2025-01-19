students = [{"name":"Hermione","house":"Greffindor","patrouns":"otter"},
            {"name":"Harry","house":"Greffindor","patrouns":"stag"},
            {"name":"Ron","house":"Greffindor","patrouns":"jack russell terrier"},
            {"name":"Draco","house":"slytherin","patrouns":None}
]
for student in students:
    print(student["name"],student["house"],student["patrouns"],sep=",")