import math

def minimum_distance():
    points = []

    while True:
        line = input().strip()
        x, y, z = map(int, line.split())
        points.append((x, y, z))
        if x == 0 and y == 0 and z == 0:
            break

    min_distance = float("inf")
    num_points = len(points)

    for i in range(num_points):
        for j in range(i + 1, num_points):
            x1, y1, z1 = points[i]
            x2, y2, z2 = points[j]
            distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
            if distance < min_distance:
                min_distance = distance

    print(f"{min_distance:.3f}")

minimum_distance()
