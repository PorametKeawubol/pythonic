def reverse_strings():
    while True:
        line = input()
        if line == "#":
            break
        print(line[::-1])
reverse_strings()
