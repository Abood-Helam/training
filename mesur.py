def printInfo():
    print("#######################################\n",
          "hello to the converter calculator\n",
          "kg       converts kelogram to bound\n",
          "m        converts meter to kelometers\n",
          "b        bound to kg\n",
          "km       km to m\n",
          "f        f to c\n",
          "c        c to f\n",
          "quit     ends the program")
    
while True:
    printInfo()
    help = input(">")
    if help == "kg":
        n=float(input("your wight: "))
        print(f"{n/0.453} bounds")
    elif help == "b":
        n=float(input("your wight: "))
        print(f"{n*0.453} kg")
    elif help == "m":
        n = float(input("length in meter: "))
        print(f"{n/1000} km")
    elif help == "km":
        n = float(input("length in km: "))
        print(f"{n*1000} m")
    elif help == "f":
        n = float(input("enter the temperature in fahrenheit: "))
        print(f"{(n-32)*5/9}  c")
    elif help == "c":
        n = float(input("enter the temprature in celeceus: "))
        print(f"{(n*5/9)+32}  f")
    elif help =="help":
        continue
    elif help =="quit":
        print("thanks")
        break
    else:
        print("what? ")
        break


    
