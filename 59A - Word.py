n = input()

string = ""
ucase = 0
lcase = 0

for i in range(len(n)):
    if n[i].islower():
        lcase = lcase + 1
    else:
        ucase = ucase + 1
        
if lcase >= ucase:
    for j in range(len(n)):
        if n[j].isupper():
            string = string + n[j].lower()
        else:
            string = string + n[j]
            
else:
    for j in range(len(n)):
        if n[j].islower():
            string = string + n[j].upper()
        else:
            string = string + n[j]
    
            
        
print(string)
