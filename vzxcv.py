def shoewer(n, s, m):
    time = []
    for _ in range(n):
        li, ri = map(int, input().split())
        time.append((li, ri))
    current_time = 0
    
    for li, ri in time:
        if li - current_time >= s:
            return "Yes"
        current_time = ri
    
    if m - current_time >= s:
        return "Yes"
    
    return "No"

t = int(input())
for i in range(t):
    n, s, m = map(int, input().split())
    print(shoewer(n, s, m))
