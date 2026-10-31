n=int(input())
f=[]
d=2
while d*d<=a:
    if n%d==0:
        f.append(d)
        a//=d
    else:
        d+=1
if n>1:
    f.append(a)
print(*f)
