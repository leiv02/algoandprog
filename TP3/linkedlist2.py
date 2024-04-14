class Node:
    def __init__(self, data):
        self.data = data
        self.precedent = None
        self.suivant = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        actuel = self.head
        while actuel.suivant:
            actuel = actuel.suivant
        actuel.suivant = new_node
        new_node.precedent = actuel

    def affiche(self):
        actuel = self.head
        while actuel:
            print(actuel.data, end=" ")
            actuel = actuel.suivant
        print()

    def add_at_position(self, data, position):
        if position == 0:
            new_node = Node(data)
            new_node.suivant = self.head
            if self.head:
                self.head.precedent = new_node
            self.head = new_node
            return
        actuel = self.head
        for _ in range(position - 1):
            if actuel is None:
                raise IndexError("Position out of bounds")
            actuel = actuel.suivant
        if actuel is None:
            raise IndexError("Position out of bounds")
        new_node = Node(data)
        new_node.precedent = actuel
        new_node.suivant = actuel.suivant
        if actuel.suivant:
            actuel.suivant.precedent = new_node
        actuel.suivant = new_node

    def remove_at_position(self, position):
        if position == 0:
            if self.head:
                self.head = self.head.suivant
                if self.head:
                    self.head.precedent = None
                return
            else:
                raise IndexError("List is empty")
        actuel = self.head
        for _ in range(position):
            if actuel is None:
                raise IndexError("Position out of bounds")
            actuel = actuel.suivant
        if actuel is None:
            raise IndexError("Position out of bounds")
        if actuel.precedent:
            actuel.precedent.suivant = actuel.suivant
        if actuel.suivant:
            actuel.suivant.precedent = actuel.precedent

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
        new_node.precedent = actuel
        new_node.suivant = actuel.suivant
        if actuel.suivant:
            actuel.suivant.precedent = new_node
        actuel.suivant = new_node

    @staticmethod
    def merge_sorted_lists(list1, list2):
        merged = DoublyLinkedList()
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


# Doubly Linked list
dll = DoublyLinkedList()
dll.append(1)
dll.append(3)
dll.append(5)
dll.append(8)
dll.append(9)
dll.append(12)
dll.append(20)
dll.affiche()

# Add element at specific position
dll.add_at_position(7, 4)
dll.affiche()

# Remove element at specific position
dll.remove_at_position(4)
dll.affiche()

# Length of doubly linked list
print("Length:", dll.length())

# Get position of specific element
print("Position of 9:", dll.find_position_of_element(9))

# Add element in sorted manner
dll.add_sorted(7)
dll.affiche()

# Merge two sorted lists
dll2 = DoublyLinkedList()
dll2.append(2)
dll2.append(4)
dll2.append(6)
dll2.append(10)
merged = DoublyLinkedList.merge_sorted_lists(dll, dll2)
merged.affiche()
