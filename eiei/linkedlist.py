#Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next

def main():
    head = Node(1)
    second = Node(2)
    third = Node(3)

    head.next = second
    second.next = third

    print_list(head)

if __name__ == "__main__":
    main()
