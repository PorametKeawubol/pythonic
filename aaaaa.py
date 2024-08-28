import math
n,m,a= map(int, input().split())
area = n*m
stone = a*a
if area / stone <= 1:
    print(1)
elif a == 1:
    print(area)
elif area / stone > 1:
    x = math.ceil(n/a)*math.ceil(m/a)
    print(x)

            

