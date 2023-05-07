from LinkedList.singly import LinkedList

# Create a new LinkedList
LL = LinkedList()

# Append 1 to the LinkedList
LL.append(1)
# LinkedList: 1->None

# Prepend 2 to the LinkedList
LL.prepend(2)
# LinkedList: 2->1->None

# Insert 3 at position 1 in the LinkedList
LL.insert(3, 1)
# LinkedList: 2->3->1->None

# Delete 3 from the LinkedList
LL.delete(3)
# LinkedList: 2->1->None
LL.append(5)
LL.append(6)
LL.append(7)
LL.append(8)
LL.append(9)
# Search for 1 in the LinkedList
index = LL.search(1)
print("Index of 1:", index)
# Output: Index of 1: 1

# Reverse the LinkedList
LL.reverse()
# LinkedList: 1->2->None

# Rotate the LinkedList 1 step to the right
LL.rotate(1)
# LinkedList: 2->1->None
LL.display()
# Rotate the LinkedList 1 step to the left
LL.rotate(-1)
# LinkedList: 1->2->None

# Display the LinkedList
LL.display()
# Output: 1->2->None
print(LL.length())
