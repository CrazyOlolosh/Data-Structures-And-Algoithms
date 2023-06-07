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
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index - 1)
        removed = temp.next
        temp.next = removed.next
        removed.next = None
        self.length -= 1
        return removed

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node(self):
        slow = self.head
        if not slow:
            return None
        fast = slow.next
        while fast != None:
            slow = slow.next
            fast = fast.next
            if fast.next is None:
                print(slow.value)
                return slow
            else:
                fast = fast.next
        print(slow.value, fast.value)

    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, m, n):
        if self.length <= 1:
            return None
        if m == n:
            return self
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        for _ in range(m):
            prev = prev.next
        current = prev.next
        for _ in range(n - m):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
        self.head = dummy.next
        return self

    def partition_list(self, x):
        if self.length == 0:
            return None
        small_list = LinkedList(0)
        large_list = LinkedList(0)
        prev1 = small_list
        prev2 = large_list
        current = self.head
        while current is not None:
            if current.value < x:
                prev1.next = current
                prev1 = prev1.next
            else:
                prev2.next = current
                prev2 = prev2.next
            current = current.next
        prev1.next = None
        prev2.next = None
        prev1.next = large_list.next
        self.head = small_list.next
        return self

    # O(n^2)
    # def remove_duplicates(self):
    #     if self.length == 0:
    #         return None
    #     current = self.head
    #     while current is not None:
    #         runner = current
    #         while runner.next is not None:
    #             if runner.next.value == current.value:
    #                 runner.next = runner.next.next
    #             else:
    #                 runner = runner.next
    #         current = current.next

    # O(n)
    def remove_duplicates(self):
        values = set()
        prev = None
        current = self.head
        while current is not None:
            if current.value in values:
                prev.next = current.next
                self.length -= 1
            else:
                values.add(current.value)
                prev = current
            current = current.next


def find_kth_from_end(ll: LinkedList, k):
    slow = ll.head
    fast = ll.head
    for _ in range(k):
        fast = fast.next
        if fast is None:
            return None
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow


my_linked_list = LinkedList(1)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(4)
my_linked_list.remove_duplicates()

my_linked_list.print_list()
