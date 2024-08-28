MOD = 1000000007

def mod_inverse(a, p):
    return pow(a, p - 2, p)

def card_dealer_game(n, decks):
    dp = [0] * (n + 1)
    dp[n] = 1  
    
    for i in range(n - 1, -1, -1):
        p, q = decks[i]
        total = p + q
        red_prob = p * mod_inverse(total, MOD) % MOD
        blue_prob = q * mod_inverse(total, MOD) % MOD
        
        dp[i] = (red_prob * dp[i + 1] + blue_prob * (1 - dp[i + 1] + MOD)) % MOD
    

    return dp[0]


n = int(input())
decks = []
for _ in range(n):
    p, q = map(int, input().split())
    decks.append((p, q))


result = card_dealer_game(n, decks)
print(result)
