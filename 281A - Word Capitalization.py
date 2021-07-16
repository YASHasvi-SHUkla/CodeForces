
string = input()
string1 = ''
if string[0].islower():
    string1 = string[0].upper() + string[1:]
    print(string1)
else:
    print(string)
    
