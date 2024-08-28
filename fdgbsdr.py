def farmer(a):
    xx = a//4
    x = a % 4
    if x == 0:
        return xx
    elif x == 2:
        return xx + 1
    else: return xx
    




n = int(input())

for i in range(n):
    a = int(input())
    print(farmer(a))

    
