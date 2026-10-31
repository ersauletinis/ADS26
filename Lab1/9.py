from collections import deque
t=int(input())
for _ in range(t):
    n=int(input())
    d=deque(range(n))
    ans=[0]*n
    for i in range(1,n+1):
        d.rotate(-(i%len(d)))
        p=d.popleft()
        ans[p]=i
    print(*ans)

