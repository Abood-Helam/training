import re
email = input("enter your email: ").strip()
if re.search(r"^(\w+\.)\w+@(\w+\.)?\w+\.com$", email , re.IGNORECASE):
    print("valid")
else:
    print("invalid")