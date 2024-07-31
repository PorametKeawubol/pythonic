def calculate_average():
    n = int(input()) 
    e = []

    while True:
        line = input().split()  
        numbers = list(map(int, line))  
        e.extend(numbers)  
        if len(e) >= n:
              
            break

    average = sum(e) / n 
    print(f"{average:.2f}") 

calculate_average()
