
def max_rectangle_area(n, lengths):
    # Sort lengths in descending order
    lengths.sort(reverse=True)
    
    # List to store the side lengths of the rectangle
    sides = []
    
    i = 0
    while i < n - 1:
        # If we find a pair, add it to the sides list
        if lengths[i] == lengths[i + 1]:
            sides.append(lengths[i])
            i += 2  # Move past this pair
        else:
            i += 1  # Move to the next chopstick
    
    # If we have at least two different pairs, calculate the area
    if len(sides) >= 2:
        return sides[0] * sides[1]
    else:
        return 0

# Input reading
n = int(input())
lengths = list(map(int, input().split()))

# Function call and output
print(max_rectangle_area(n, lengths))
