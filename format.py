import re

name = input("enter your name: ").strip()
if matches :=re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
