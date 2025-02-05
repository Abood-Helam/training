notes = ["i like apple",]

def add():
    new = input("new note: ")
    notes.append(new)

def apper():
    print(notes)

def save():
    save(notes)

#def d():
#    n = init(input("which note: "))
#    notes.__delattr__([n])

while True:
    print("""#########################
add       write a new note 
show      print all notes
save      save the notes
quit      exit from the program""")
    h = input(">")
    if h == "add":
        add()
    elif h == "show":
        apper()
#    elif h == "save":
#        save()
    elif h == "quit":
        print("thanks")
        break
    elif h == "help":
        continue
    else:
        print("what?")
        continue