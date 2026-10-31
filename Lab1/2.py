b,c,a=map(int,input().split())
s=1
while c!=0:
    if c%2==0:
        b=b*b%a
        c//=2
    else:
        s=s*b%a
        c-=1
sum=s%a
print(sum)


