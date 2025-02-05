store = []

class Item:
    def __init__(self, name, date, color, size, quantity):
        self.name: str = name
        self.date: float = date
        self.color: str = color
        self.size: str = size
        self.quantity:int = quantity
    def print_me(self):
        print(f"name: {self.name},date: {self.date}, color: {self.color}, size: {self.size}, quantity: {self.quantity}")

    def toJson(self):
        return json.dumps(self, default=lambda o:o.__dict__)
        
        
def add_object():
    name = input("enter the name of the opject: ")
    size = input("enter the size of the opject: ")
    date = (input("enter the expire date of the opject: "))
    color = input("enter the color of the opject: ")
    quantity = (input("enter how many opject there is in the store: "))
    l = Item(name,size, date, color, quantity)
    store.append(l)

    print("the opject has been added")

def search_object():
    search = input("enter the name of the opject: ")
    for n in store:
        if n.name == search:
            n.print_me()
        else:
            print("ronge name please try again")
            
def delet_object():
    d = input("enter the name of the opject you want to delet: ")
    for n in store:
        if n.name == d:
            store.remove(n)

import json 
import os

TASKS_FILE = "store.txt"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for item in file.readlines():
                store.append(json.load(item))    

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        for item in store:
            file.write(f"{item.name}, {item.size}, {item.date}, {item.color}, {item.quanti}")

def show_tasks():
    if not store:
        print('there is no items in the store yet')
    else:
        print('the items are')
        for i in store:
            i.print_me() 
            print("\n")       

def main():
    load_tasks()
    while True:
        help = input(">")
        if help == "add":
            add_object()
        elif help == "search":
            search_object()
        elif help == "delet":
            delet_object()
        elif help == "show":
            show_tasks()
        elif help == "save":
            save_tasks()
        elif help == "help" :
            print("""
                  add   to add new opject
                  sve   to save the information and quit
                  quit  to exit the program
                  delet to delet a sobject""")
        elif help == "quit":
            print("thanks")
            break
        else:
            print("what? ")
            continue 



if __name__ == "__main__":
    main()       



