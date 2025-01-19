def main():
    print_square(3)

#def print_square(size):
#    for i in range(size):
#        print("#",end="")
#        for j in range(size):
#            print("#",end="")

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#",width)
main()