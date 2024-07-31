from itertools import combinations

def solve_dot_problem(N, M, abilities):
    max_dot = 0
    max_time = 0
    
    for r in range(1, M + 1):
        for comb in combinations(abilities, r):
            total_dps = sum(dps for dps, _ in comb)
            min_duration = min(duration for _, duration in comb)
            if total_dps > max_dot or (total_dps == max_dot and min_duration > max_time):
                max_dot = total_dps
                max_time = min_duration
    
    print(max_dot, max_time)

# Read input
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    
    abilities = []
    index = 2
    for _ in range(N):
        dps = int(data[index])
        duration = int(data[index + 1])
        abilities.append((dps, duration))
        index += 2
    
    solve_dot_problem(N, M, abilities)

if __name__ == "__main__":
    main()
