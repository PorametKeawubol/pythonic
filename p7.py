from bisect import bisect_left

def tree():
    n = int(input()) 
    e = []

    while True:
        line = input().split()
        numbers = list(map(int, line))
        e.extend(numbers)

        if len(e) >= n:
            sub = []
            for x in e:
                if len(sub) == 0 or sub[-1] < x:
                    sub.append(x)
                else:
                    idx = bisect_left(sub, x)
                    sub[idx] = x
            print(len(sub))
            break

tree()
