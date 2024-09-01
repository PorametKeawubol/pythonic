def eiei(s):
    max1 = max(s)  
    s.remove(max1) 
    max2 = max(s)  
    return max1 * max2 

n = int(input())
s = []

while len(s) < n:
    x = input()
    i = list(map(int, x.split())) 
    s.extend(i) 

print(eiei(s))
