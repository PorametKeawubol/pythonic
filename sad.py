def check_min_cost(mydict, required_stats, K):
    required_mask = 0
    for stat in required_stats:
        required_mask |= (1 << (stat - 1))
    
    # DP Table for storing minimum cost for each possible stat combination
    dp = [float('inf')] * (1 << K)
    dp[0] = 0  # No cost to cover no stats

    for price, stat_mask in mydict:
        for mask in range((1 << K) - 1, -1, -1):
            dp[mask | stat_mask] = min(dp[mask | stat_mask], dp[mask] + price)

    # Return the minimum cost to achieve the required mask
    return dp[required_mask] if dp[required_mask] != float('inf') else -1

# Reading input
N, M, K = map(int, input().split())

mydict = []
for _ in range(N):
    stite, price = map(int, input().split())
    numbers = list(map(int, input().split()))
    
    # Create bitmask for the potion's stat coverage
    stat_mask = 0
    for num in numbers:
        stat_mask |= (1 << (num - 1))
    
    mydict.append((price, stat_mask))

results = []
for _ in range(M):
    m = int(input())
    required_stats = list(map(int, input().split()))
    
    # Calculate the minimum cost for each day's requirement
    min_cost = check_min_cost(mydict, required_stats, K)
    results.append(min_cost)

# Print results
for result in results:
    print(result)
