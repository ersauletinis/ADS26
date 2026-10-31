def ers(n):
    stk=[]
    stk1=[]
    for i in n:
        while stk and stk[-1]>=i:
            stk.pop()
        if not stk:
            stk1.append(-1)
        else:
            stk1.append(stk[-1])
        stk.append(i)
    return stk1
d=int(input())
s=list(map(int ,input().split()))
print(*ers(s))
        

    