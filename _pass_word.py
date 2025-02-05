import re
pass_word = input("pass word: ")
if re.search(r"^\w+\.$", pass_word, re.IGNORECASE):
    print("valid")
else:
    print("invalid")
count = 0
limit = 3
while count < limit:
    pd = input("enter pass word: ")
    
    count += 1 
    if pd == pass_word:
        print("passed")
        break
    elif pd != pass_word and count < limit:
        print("try again")
    else:
        print("out of tries!")
        break






