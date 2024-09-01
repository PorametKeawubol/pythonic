#Circular Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    temp = head

    if head is not None:
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == head:
                break

def main():
    head = Node(1)
    second = Node(2)
    third = Node(3)

    head.next = second
    second.next = third
    third.next = head

    print_list(head)

if __name__ == "__main__":
    main()