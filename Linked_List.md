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
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

```

---
## 🔹 Program 2: Double Linked List – All Basic Operations

```python
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None


    # Insert at beginning
    def insert_at_beg(self, data):
        new_node = DNode(data)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node


    # Insert at end
    def insert_at_end(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp


    # Insert at kth position
    def insert_at_kth(self, k, data):
        if k == 1:
            self.insert_at_beg(data)
            return
        temp = self.head
        count = 1
        while temp and count < k - 1:
            temp = temp.next
            count += 1
        if not temp:
            return
        new_node = DNode(data)
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node


    # Delete at beginning
    def delete_at_start(self):
        if not self.head:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None


    # Delete at end
    def delete_at_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None


    # Delete at kth position
    def delete_at_kth(self, k):
        if not self.head:
            return
        if k == 1:
            self.delete_at_start()
            return
        temp = self.head
        count = 1
        while temp and count < k:
            temp = temp.next
            count += 1
        if not temp:
            return
        if temp.next:
            temp.next.prev = temp.prev
        temp.prev.next = temp.next


    # Search
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False


    # Traverse
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")
```

---
---
## 🔹 Program 3: Circular Linked List – All Basic Operations

```python
class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None


    # Insert at beginning
    def insert_at_beg(self, data):
        new_node = CNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        new_node.next = self.head
        temp.next = new_node
        self.head = new_node


    # Insert at end
    def insert_at_end(self, data):
        new_node = CNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head


    # Insert at kth position
    def insert_at_kth(self, k, data):
        if k == 1:
            self.insert_at_beg(data)
            return
        if not self.head:
            return
        new_node = CNode(data)
        temp = self.head
        count = 1
        while temp.next != self.head and count < k - 1:
            temp = temp.next
            count += 1
        new_node.next = temp.next
        temp.next = new_node


    # Delete at beginning
    def delete_at_start(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next


    # Delete at end
    def delete_at_end(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
            return
        prev = None
        temp = self.head
        while temp.next != self.head:
            prev = temp
            temp = temp.next
        prev.next = self.head


    # Delete at kth position
    def delete_at_kth(self, k):
        if not self.head:
            return
        if k == 1:
            self.delete_at_start()
            return
        temp = self.head
        count = 1
        while temp.next != self.head and count < k - 1:
            temp = temp.next
            count += 1
        if temp.next != self.head:
            temp.next = temp.next.next


    # Search an element
    def search(self, key):
        if not self.head:
            return False
        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False


    # Traverse the list
    def traverse(self):
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
```

---
