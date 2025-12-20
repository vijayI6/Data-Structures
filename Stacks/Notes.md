
A **Stack** is a linear and Dynamic data structure that follows the **LIFO (Last In, First Out)** principle.

👉 The element added **last** is removed **first**.

---

## Key Characteristics of Stack

- Follows **LIFO** order
- Insertion and deletion happen only at **one end** called **TOP**
- Stack operations are efficient (**O(1)** time complexity)
- Used heavily in **DSA, compilers, and real-world applications**

---

## Basic Stack Operations

| Operation | Description |
|---------|-------------|
| Push | Insert an element at the top |
| Pop | Remove the top element |
| Peek | View the top element without removing |
| isEmpty | Check if stack is empty |
| isFull | Check if stack is full (fixed-size stack) |
| Size | Get number of elements |

---

## Stack Implementation using Array

```python
class Stack:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity


    # Push operation
    def push(self, item):
        if self.is_full():
            print("Stack Overflow! Cannot push", item)
        else:
            self.stack.append(item)
            print(f"{item} pushed into stack")


    # Pop operation
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop")
            return None
        else:
            return self.stack.pop()


    # Peek operation
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            return self.stack[-1]


    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0


    # Check if stack is full
    def is_full(self):
        return len(self.stack) == self.capacity


    # Get stack size
    def size(self):
        return len(self.stack)


# Create a stack of capacity 3
s = Stack(3)

# Push elements
s.push(10)
s.push(20)
s.push(30)

# Try pushing when stack is full
s.push(40)

# Peek top element
print("Top element:", s.peek())

# Pop an element
print("Popped element:", s.pop())

# Check stack size
print("Current stack size:", s.size())

# Check if stack is empty
print("Is stack empty?", s.is_empty())

```

---

# Stack Implementation Using Linked List 

```python
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack class using Linked List
class Stack:
    def __init__(self):
        self.top = None
        self.count = 0


    # Push operation
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.count += 1
        print(f"{item} pushed into stack")


    # Pop operation
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop")
            return None
        popped = self.top.data
        self.top = self.top.next
        self.count -= 1
        return popped


    # Peek operation
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.top.data


    # Check if stack is empty
    def is_empty(self):
        return self.top is None


    # Get stack size
    def size(self):
        return self.count


# Create stack object
s = Stack()

# Push elements
s.push(10)
s.push(20)
s.push(30)

# Peek top element
print("Top element:", s.peek())

# Pop element
print("Popped element:", s.pop())

# Check stack size
print("Stack size:", s.size())

# Check if stack is empty
print("Is stack empty?", s.is_empty())
