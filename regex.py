import re

with open("regex_test.txt")as names:
    data = names.readlines()

for name in data:
    pattern = re.match(r'[A-Z, a-z]+[" "][A-Z][- a-z, A-Z]+', name)
   
    if pattern:
        print(pattern.group())
    
    else:
        print(None)
