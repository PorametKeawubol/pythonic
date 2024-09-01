def solve():
    from collections import defaultdict
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    M = int(data[idx + 1])
    K = int(data[idx + 2])
    idx += 3
    
    inf = float('inf')
    min_cost = defaultdict(lambda: inf)
    
    # Processing potions
    for _ in range(N):
        n = int(data[idx])
        c = int(data[idx + 1])
        idx += 2
        stats_mask = 0
        for i in range(n):
            stat = int(data[idx + i]) - 1
            stats_mask |= (1 << stat)
        idx += n
        
        min_cost[stats_mask] = min(min_cost[stats_mask], c)
    
    # Prepare DP for all combinations of stats
    dp = [inf] * (1 << K)
    dp[0] = 0
    
    for mask in range(1 << K):
        for potion_mask, cost in min_cost.items():
            combined_mask = mask | potion_mask
            dp[combined_mask] = min(dp[combined_mask], dp[mask] + cost)
    
    results = []
    
    # Processing days
    for _ in range(M):
        m = int(data[idx])
        required_mask = 0
        for i in range(m):
            stat = int(data[idx + i]) - 1
            required_mask |= (1 << stat)
        idx += m
        
        if dp[required_mask] == inf:
            results.append('-1')
        else:
            results.append(str(dp[required_mask]))
    
    print("\n".join(results))

# Example to run solve()
if __name__ == "__main__":
    solve()
