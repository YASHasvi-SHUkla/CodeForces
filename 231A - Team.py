t = int(input())
yash = 0

for i in range(t):
    
    ls = list(map(int,input().split()))
    
    if ls.count(1)>=2:
        yash = yash + 1
        
print(yash)
    
