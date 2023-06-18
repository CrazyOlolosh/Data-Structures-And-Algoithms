class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def bubble_sort(self):
        temp = self.head
        while temp.next is not None:
            if temp.value > temp.next.value:
                temp.value, temp.next.value = temp.next.value, temp.value
            temp = temp.next
        temp = self.head
        while temp.next is not None:
            if temp.value > temp.next.value:
                self.bubble_sort()
            temp = temp.next

    def alt_bubble_sort(self):
        # Check if the list has less than 2 elements
        if self.length < 2:
            return

        # Initialize the sorted_until pointer to None
        sorted_until = None

        # Continue sorting until sorted_until reaches the second node
        while sorted_until != self.head.next:
            # Initialize current pointer to head of the list
            current = self.head

            # Iterate through unsorted portion of the list until sorted_until
            while current.next != sorted_until:
                next_node = current.next

                # Swap current and next_node values if current is greater
                if current.value > next_node.value:
                    current.value, next_node.value = next_node.value, current.value

                # Move current pointer to next node
                current = current.next

            # Update sorted_until pointer to the last node processed
            sorted_until = current


my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.bubble_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""
