import math 
lst=list(map(int,input().split()))
a=lst[0]
b=lst[1]
print(math.gcd(a,b))

#------2

def gcd(a,b):
    while b:
       a,b=b, a%b
    return a

lst=list(map(int,input().split()))
a=lst[0]
b=lst[1]


print(gcd(a,b))

#------3

from math import gcd
a,b=map(int,input().split())
print(gcd(a,b))

