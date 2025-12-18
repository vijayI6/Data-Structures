# 🎙️ Linked List

A **Linked List** is a **Linear Data Structure** where each element is called a **node**.
Each node contains **two fields**:

* **Data field** → Stores the information
* **Next (Address) field** → Stores the address of the next node

👉 Linked lists allow **efficient insertion and deletion** compared to arrays.

---

## 🎙️ Types of Linked List

* **Singly Linked List**
* **Doubly Linked List**
* **Circular Linked List**

---

## 📊 Array vs Linked List

| Array                                           | Linked List                                                |
| ----------------------------------------------- | ---------------------------------------------------------- |
| Fixed size                                      | Dynamic size                                               |
| Fast access using index                         | Slow access (sequential traversal)                         |
| Insertion & deletion in middle is costly (O(n)) | Insertion & deletion is efficient (O(1) if position known) |
| Stored in contiguous memory                     | Stored in non-contiguous memory                            |

---


## 🔹 Program 1: Singly Linked List – All Basic Operations

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None


    # Insert at beginning
    def insert_at_beg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node


    # Insert at kth position
    def insert_at_kth(self, k, data):
        new_node = Node(data)
        if k == 1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        count = 1
        while temp and count < k - 1:
            temp = temp.next
            count += 1
        if not temp:
            return
        new_node.next = temp.next
        temp.next = new_node


    # Delete at beginning
    def delete_at_start(self):
        if self.head:
            self.head = self.head.next


    # Delete at end
    def delete_at_end(self):
        if not self.head or not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None


    # Delete at kth position
    def delete_at_kth(self, k):
        if not self.head:
            return
        if k == 1:
            self.head = self.head.next
            return
        temp = self.head
        count = 1
        while temp.next and count < k - 1:
            temp = temp.next
            count += 1
        if temp.next:
            temp.next = temp.next.next


    # Search element
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False


    # Traverse list
    def traverse(self):   # single and double
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


    def traverse_circular(self):     # for circular linked list
        if not self.head:
            print("Circular Linked List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")


    # Reverse list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Driver Code
sll = SinglyLinkedList()
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.insert_at_beg(5)

print("Linked List:")
sll.traverse()

print("After inserting at 3rd position:")
sll.insert_at_kth(3, 15)
sll.traverse()

print("After deleting last element:")
sll.delete_at_end()
sll.traverse()

print("Searching 20:", sll.search(20))

print("Reversed Linked List:")
sll.reverse()
sll.traverse()
```

---
