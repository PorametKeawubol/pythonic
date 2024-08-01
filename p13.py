
n = int(input())
e = []


for i in range(n):
    line = int(input())
    e.append(line)

m = max(e)

def create_triangle_dict(m):
    triangle_dict = {}
    vertices = 1
    triangles = 0
    increment_vertices = 2
    increment_triangles = 1

    while vertices <= m:
        triangle_dict[vertices] = triangles
        vertices += increment_vertices
        increment_vertices += 1
        triangles += increment_triangles
        increment_triangles += 2

    return triangle_dict

def max_triangles(n, triangle_dict):
    remaining_points = n
    max_triangles = 0
    sorted_keys = sorted(triangle_dict.keys(), reverse=True)
    
    for key in sorted_keys:
        while remaining_points >= key:
            remaining_points -= key
            max_triangles += triangle_dict[key]
    
    return max_triangles


triangle_dict = create_triangle_dict(m)

for points in e:
    max_triangles_count = max_triangles(points, triangle_dict)
    print(max_triangles_count)
