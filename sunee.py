def gamecard(a):
    a1, a2, b1, b2 = int(a[0]), int(a[1]), int(a[2]), int(a[3])
    
    scenarios = [
        (a1, b1, a2, b2), 
        (a1, b2, a2, b1), 
        (a2, b1, a1, b2), 
        (a2, b2, a1, b1)  
    ]
    
    win_count = 0
    for s1, s2, s3, s4 in scenarios:
        suneet_wins = (s1 > s2) + (s3 > s4)
        slavic_wins = (s1 < s2) + (s3 < s4)
        
        if suneet_wins > slavic_wins:
            win_count += 1
    
    return win_count

n = int(input())

for i in range(n):
    a = input().split()
    print(gamecard(a))
