def absolute_majority(T, cases):
    results = []
    for t in range(T):
        N, C = cases[t][0]
        votes = cases[t][1]
        
        # Filter out invalid votes
        valid_votes = [vote for vote in votes if 1 <= vote <= C]
        total_valid_votes = len(valid_votes)
        
        # Count votes for each candidate
        vote_count = [0] * (C + 1)
        for vote in valid_votes:
            vote_count[vote] += 1
        
        # Check for absolute majority
        has_majority = False
        for count in vote_count:
            if count > total_valid_votes / 2:
                has_majority = True
                break
        
        # Record the result
        if has_majority:
            results.append(f"Case {t + 1}: Yes")
        else:
            results.append(f"Case {t + 1}: No")
    
    return results

# Example usage:
T = 3
cases = [
    ((15, 3), [1, 1, 2, 1, 3, 1, 1, 1, 1, 3, 3, 2, 2, 2, 1]),
    ((15, 3), [1, 1, 2, 1, 3, 1, 3, 1, 1, 3, 3, 2, 2, 2, 3]),
    ((10, 2), [1, 2, 1, 2, 3, 1, 2, 1, 2, 3])
]
print("\n".join(absolute_majority(T, cases)))
