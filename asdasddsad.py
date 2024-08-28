def is_sub(s, t):
    index = 0
    for value in t:
        index = s.find(value, index)
        if index == -1:
            return "NO"
        index += 1
    return "YES"

def replace_first_mismatch(s, t_str):
    s_list = list(s)
    index_s, index_t = 0, 0
    
    while index_s < len(s_list) and index_t < len(t_str):
        if s_list[index_s] == t_str[index_t]:
            index_t += 1
        elif s_list[index_s] == '?':
            s_list[index_s] = t_str[index_t]
            index_t += 1
        index_s += 1
    
    return ''.join(s_list)

def replace_questions(s, t_str):
    s_list = list(s)
    t_index = 0
    
    for i in range(len(s_list)):
        if s_list[i] == '?':
            s_list[i] = t_str[t_index]
            t_index = (t_index + 1) % len(t_str)

    return ''.join(s_list)

t = int(input())
for _ in range(t):
    s = input()
    t_str = input()
    
    # Check if t_str is already a subsequence of s
    if is_sub(s, t_str) == "NO":
        # Try to make t_str a subsequence by replacing '?' accordingly
        s = replace_first_mismatch(s, t_str)
    
    # Replace any remaining '?' in s with characters from t_str
    s = replace_questions(s, t_str)
    
    # Final check if t_str is now a subsequence of s
    result = is_sub(s, t_str)
    print(result)
    if result == "YES":
        print(s)
