a=int(input())
res = True
for i in range(2,int(a**0.5)+1):
    if a % i == 0:
        res = False
if res:
    print("YES")
else:
    print("NO")

