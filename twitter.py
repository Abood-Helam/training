import re

url = input("enter your url: ")

#username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
#print(f"username: {username}")

matches = re.search(r"^(?:https?://)(?:www\.)twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"username: ", matches.group(1))