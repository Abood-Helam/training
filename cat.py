#i = 3
#while i != 0:
#    print("meow") 
#    i = i-1
#i = 0
#while i<3:
#    print("meow")
#    i+=1
#for i in [0,1,2]:
#    print("meow")
#for _ in range(3):
#    print("meow")


def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("what is n? "))
        if n >0:
            break
    return n
    
def meow(n):
    for _ in range(n):
        print("meow")
main()

