class Wizard:
    def __init__ (self, name):
        if not name:
            raise ValueError("missing name!")
        self.name = name

    ...

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
    ...

class Professor(Wizard):
    def __init__(self, name, opject):
        super().__init__(name)
        self.opject = opject
    ...
    

wizard = Wizard("albus")
student = Student("Harry", "Gryffindor")
professor = Professor("severus", "defense against the dark arts")