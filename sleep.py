def main():
    n = int(input("what's n? "))
    for i in range(n):
        print("sh"*i)

if __name__ == "__main__":
    main()

def main():
    n = int(input("what's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "sh" * i

if __name__ == "__main__":
    main()