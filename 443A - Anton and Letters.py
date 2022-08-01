s = input()
draken = ""

for i in s:
    if ord(i) >= 65 and ord(i) <= 122:
        draken = draken + i
print(len(set(list(draken))))
