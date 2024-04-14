class Node:
    def __init__(self, data):
        self.data = data
        self.suivant = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.suivant:
            last_node = last_node.suivant
        last_node.suivant = new_node

    def affiche(self):
        actuel = self.head
        while actuel:
            print(actuel.data , end=" ")
            actuel = actuel.suivant
        print()

    def add_at_position(self, data, position):
        if position == 0:
            new_node = Node(data)
            new_node.suivant = self.head
            self.head = new_node
            return
        actuel = self.head
        for _ in range(position - 1):
            if actuel is None:
                raise IndexError("position out of bound")
            actuel = actuel.suivant
        if actuel is None:
            raise IndexError("position out of bound")
        new_node = Node(data)
        new_node.suivant = actuel.suivant
        actuel.suivant = new_node

    def remove_at_position(self, position):
        if position == 0:
            if self.head:
                self.head = self.head.suivant
                return
            else:
                raise IndexError("list is empty")
        actuel = self.head
        prev = None
        for _ in range(position):
            if actuel is None:
                raise IndexError("position out of bound")
            prev = actuel
            actuel = actuel.suivant
        if actuel is None:
            raise IndexError("position out of bound")
        prev.suivant = actuel.suivant

    def length(self):
        actuel = self.head
        count = 0
        while actuel:
            count += 1
            actuel = actuel.suivant
        return count

    def find_position_of_element(self, value):
        actuel = self.head
        pos = 0
        while actuel:
            if actuel.data == value:
                return pos
            actuel = actuel.suivant
            pos += 1
        return -1

    def add_sorted(self, data):
        if not self.head or self.head.data >= data:
            self.add_at_position(data, 0)
            return
        actuel = self.head
        while actuel.suivant and actuel.suivant.data < data:
            actuel = actuel.suivant
        new_node = Node(data)
        new_node.suivant = actuel.suivant
        actuel.suivant = new_node

    @staticmethod
    def merge_sorted_lists(list1, list2):
        merged = LinkedList()
        actuel1 = list1.head
        actuel2 = list2.head
        while actuel1 or actuel2:
            if not actuel1:
                merged.append(actuel2.data)
                actuel2 = actuel2.suivant
            elif not actuel2:
                merged.append(actuel1.data)
                actuel1 = actuel1.suivant
            elif actuel1.data <= actuel2.data:
                merged.append(actuel1.data)
                actuel1 = actuel1.suivant
            else:
                merged.append(actuel2.data)
                actuel2 = actuel2.suivant
        return merged

class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        data = self.queue.head.data
        self.queue.remove_at_position(0)
        return data

    def length(self):
        return self.queue.length()

    def is_empty(self):
        return self.queue.head is None

class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, data):
        self.stack.add_at_position(data, 0)

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        data = self.stack.head.data
        self.stack.remove_at_position(0)
        return data

    def length(self):
        return self.stack.length()

    def is_empty(self):
        return self.stack.head is None


# Linked list
ll = LinkedList()
ll.append(1)
ll.append(3)
ll.append(5)
ll.append(8)
ll.append(9)
ll.append(12)
ll.append(20)
ll.affiche()

# Add element at specific position
ll.add_at_position(7, 4)
ll.affiche()

# Remove element at specific position
ll.remove_at_position(4)
ll.affiche()

# Length of linked list
print("Length:", ll.length())

# Get position of specific element
print("Position of 9:", ll.find_position_of_element(9))

# Add element in sorted manner
ll.add_sorted(7)
ll.affiche()

# Merge two sorted lists
ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)
ll2.append(10)
merged = LinkedList.merge_sorted_lists(ll, ll2)
merged.affiche()

# Queue
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Queue length:", q.length())
print("Dequeue:", q.dequeue())

# Stack
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print("Stack length:", s.length())
print("Pop:", s.pop())
