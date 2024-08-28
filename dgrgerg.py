def is_sub(s, t):
    index = 0
    for value in t:
        index = s.find(value, index)
        if index == -1:
            return "NO",s
        index += 1
    return "Yes",s

def eiei(s):
    lst = []
    index = 0
    while index != -1:
        index = s.find("?", index)
        if index != -1:
            lst.append(index)
            index += 1 
    return lst if lst else s  

def test(s, t):
    index = 0
    x = 0
    for value in t:
        index = s.find(value, index)
        if index == -1:
            return x
        x += 1



t = int(input())
for i in range(t):
    s = str(input())
    t = str(input())
    x = (eiei(s))
    y = len(x)
    z = test(s,t)
    while y > 0:
        for i in t[z::]:
            s[x[0]] = i
            y-=1
        