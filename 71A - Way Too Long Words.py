
n = int(input())
temp = []
for i in range(1,n+1):
    name = input()
    length = len(name)
    if length > 10:
        temp.append(name[0]+str(length - 2)+name[-1])
    else:
        temp.append(name)
for j in temp:
    print(j)
