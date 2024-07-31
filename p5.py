def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def find_prime_numbers():
    n = int(input())  
    e = []

    while len(e) < n:
        line = input().split()  
        numbers = list(map(int, line))  
        e.extend(numbers) 
    
    unique_primes = set()
    
    for number in e:
        if is_prime(number):
            print(unique_primes)
            unique_primes.add(number)
    
    sorted_primes = sorted(unique_primes)
    
    print(len(sorted_primes))
    for prime in sorted_primes:
        print(prime)

find_prime_numbers()
