def ers(n):
    stack=[]
    for i in n:
        if stack and stack[-1]==i:
            stack.pop()
        else:
            stack.append(i)
    if not stack:
        return True
    else:
        return False 
        
a=input()
if ers(a):
    print("YES")
else:
    print("NO")
