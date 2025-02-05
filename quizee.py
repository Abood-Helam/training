import random 
quiz_num = random.randint(1, 10)

count = 0
limit = 3
while count < limit:
    number = int(input("what's the number? "))
    count +=1
    if number == quiz_num:
        print("correct")
        break
    elif number != quiz_num:
        print("false, please try again")
        if number < quiz_num:
            print("hint: you need a larger number")
        elif number > quiz_num:
            print("hint: you need a smaller number")
    else:
        break


    
    
