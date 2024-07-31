def reverse_strings():
    while True:
        line = input()
        if line == "#":
            break
        print(line[::-1])
reverse_strings()


def reverse_strings():  ##  อันนี้คือรับเรื่อยยๆ
    try:
        while True:
            line = input()
            print(line[::-1])
    except EOFError:
        pass

reverse_strings()


# python p2.py < test.txt > output.txt เอาไว้test