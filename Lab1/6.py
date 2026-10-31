#------1
n=input()
s=input()
c=[]
w=[]
for i in n:
    if i=="#":
        if c:
            c.pop()
    else:
        c.append(i)
for i in s:
    if i=="#":
        if w:
            w.pop()
    else:
        w.append(i)

if c==w:
    print("Yes")
else:
    print("No")

#-------2
import sys
def eq(n):
    c=[]
    for i in n:
        if i=="#":
            if c:
                c.pop()
        else:
            c.append(i)
    return c
s1=sys.stdin.readline().strip()
s2=sys.stdin.readline().strip()
if eq(s1)==eq(s2):
    print("Yes")
else:
    print("No")