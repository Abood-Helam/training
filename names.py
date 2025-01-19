names= []

for _ in range(3):
   names.append(input("Name: "))
#for name in sorted(names):
#    print(f"hello, {name}")

name = input("Name: ")
#file.open("names.txt", "a")
#file.write(f"{name}\n")
#file.close
with open ('names.txt', 'a')as file:
    file.write(f"hello,{name}\n")



#with open('names.txt') as file:
#    for line in file:
#        names.append(line.rstrip())

#for name in names:
#    print(f"hello, {name}")