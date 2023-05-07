
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def length(self):
        count = 0
        current = self.head
        while current:
            current = current.next
            count +=1
        return count

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, data, position):
        if position == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        current = self.head
        prev = None
        counter = 0
        while current and counter < position:
            prev = current
            current = current.next
            counter += 1
        if counter != position:
            raise IndexError("Position out of range")
        new_node.next = current
        prev.next = new_node

    def delete(self, data):
        if not self.head:
            raise ValueError("List is empty")
        if self.head.data == data:
            self.head = self.head.next
            return 
        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if not current:
            raise ValueError("Value not found in list")
        prev.next = current.next

    def search(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        raise ValueError("Value not found in the list")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def rotate(self, k):
        if not self.head or k == 0:
            return
        length = self.length()
        k = k % length
        rotate_ = length + k if k < 0 else length - k   # left or right depending on sign of k
        if rotate_ <= 0 or rotate_ == length:
            return
        current = self.head
        prev = None
        counter = 0
        while current and counter != rotate_:
            prev = current
            current = current.next
            counter += 1
        if not current:
            return
        new_head = current
        prev.next = None
        while current.next:
            current = current.next
        current.next = self.head
        self.head = new_head

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")