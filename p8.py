def re():
    n = int(input())
    E = []
    while True:
        line = input().split()
        num = list(map(int,line))
        E.append(num)
        if len(E) >= n:
            for i , case in enumerate(E):
                    if len(case) == 4:
                        x1, y1, x2, y2 = case
                        width = abs(x2 - x1)
                        height = abs(y2 - y1)
                        area = width * height
                    print(f"Case {i + 1}: {area:.2f}")
            break
re()       

