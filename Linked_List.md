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

## 🎙️ Creating a Node

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

---

## 🎙️ Creating a Singly Linked List

```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None
```

---

## 🎙️ Traversing a Linked List

### 🔹 Singly / Doubly Linked List

```python
def traverse(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")
```

### 🔹 Circular Linked List

```python
def traverse_circular(head):
    if not head:
        return
    temp = head
    while True:
        print(temp.data, end=" -> ")
        temp = temp.next
        if temp == head:
            break
    print("(back to head)")
```

---

## 🎙️ Searching in Linked List

```python
def searching(head, key):
    temp = head
    while temp is not None:
        if temp.data == key:
            return True
        temp = temp.next
    return False
```

---

## 🎙️ Insertion in Singly Linked List

### 🔹 Insert at Beginning

```python
def insert_at_beg(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node
```

### 🔹 Insert at End

```python
def insert_at_last(head, data):
    new_node = Node(data)
    
    if head is None:
        return new_node
    
    temp = head
    while temp.next:
        temp = temp.next
    
    temp.next = new_node
    return head
```

### 🔹 Insert at Kth Position

```python
def insert_at_kth_position(head, k, data):
    new_node = Node(data)
    
    if k == 1:
        new_node.next = head
        return new_node
    
    current = head
    count = 1
    
    while current and count < k - 1:
        current = current.next
        count += 1
    
    if not current:
        return head
    
    new_node.next = current.next
    current.next = new_node
    return head
```

---

## 🎙️ Reverse a Linked List

```python
def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev
```

---

## 🎙️ Deletion in Singly Linked List

### 🔹 Delete at Start

```python
def delete_at_start(head):
    if not head:
        return None
    return head.next
```

### 🔹 Delete at End

```python
def delete_at_end(head):
    if not head or not head.next:
        return None
    
    current = head
    while current.next.next:
        current = current.next
    
    current.next = None
    return head
```

### 🔹 Delete at Kth Position

```python
def delete_at_kth_position(head, k):
    if not head:
        return None
    
    if k == 1:
        return head.next
    
    current = head
    count = 1
    
    while current.next and count < k - 1:
        current = current.next
        count += 1
    
    if not current.next:
        return head
    
    current.next = current.next.next
    return head
```

---
