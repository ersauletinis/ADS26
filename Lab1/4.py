def ers(a):
    res = True
    for i in range(2,int(a**0.5)+1):
        if a % i == 0:
            res = False
    if res:
        return True
    else:
        return False 

s=int(input())
count=0
f=2
while True:
    if ers(f):
        count+=1
    if count==s:
        print(f)
        break
    f+=1
    
