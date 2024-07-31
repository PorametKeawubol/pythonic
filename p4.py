def find_palindrome_words():
    unique_palindromes = set()
    
    while True:
        line = input().strip()
        if line == "#":
            break
        words = line.split()
        for word in words:
           
            cleaned_word = ''.join(char.lower() for char in word if char.isalpha())
            if len(cleaned_word) >= 3 and cleaned_word == cleaned_word[::-1]:
                unique_palindromes.add(cleaned_word)
    
    sorted_palindromes = sorted(unique_palindromes)
    print(len(sorted_palindromes), " ".join(sorted_palindromes))


find_palindrome_words()

