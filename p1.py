def count_capital_letters():
    total_uppercase_count = 0
    
    while True:
        line = input()
        if line == "#":
            break
        total_uppercase_count += sum(1 for char in line if char.islower())
    
    print(total_uppercase_count)

count_capital_letters()
