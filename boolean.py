#x = int(input("what is x? "))
#if x%2==0:
#    print("x is even")
#else:
#    print("x is odd")
def main():
    x = int(input("what is x? "))
    if is_even(x):
        print("even")
    else:
        print("odd")
#def is_even(n):
#    if n%2 == 0:
#        return True
#    else:
#        return False
#def is_even(n):
#    return True if n%2==0 else False
def is_even(n):
    return n%2==0
main()   