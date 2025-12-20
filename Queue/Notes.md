A **Queue** is a **linear and Dynamic data structure** that follows the **FIFO (First In, First Out)** principle.

👉 The element that is **inserted first** is **removed first**.


---

## 📌 Key Characteristics of Queue

- Follows **FIFO** order
- Insertion happens at the **REAR**
- Deletion happens at the **FRONT**
- Efficient for scheduling and buffering
- Widely used in **DSA, OS, networking**

---

## 📌 Basic Queue Operations

| Operation | Description |
|---------|-------------|
| Enqueue | Insert an element at the rear |
| Dequeue | Remove an element from the front |
| Front / Peek | View front element without removing |
| isEmpty | Check if queue is empty |
| isFull | Check if queue is full (fixed size) |
| Size | Number of elements in queue |

---

## 📌 Queue Implementation Using Class (Python)

```python

class Queue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity


    # Enqueue operation
    def enqueue(self, item):
        if self.is_full():
            print("Queue Overflow! Cannot enqueue", item)
        else:
            self.queue.append(item)
            print(item, "enqueued to queue")


    # Dequeue operation
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Cannot dequeue")
            return None
        else:
            removed = self.queue.pop(0)
            return removed


    # Peek operation
    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[0]


    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0


    # Check if queue is full
    def is_full(self):
        return len(self.queue) == self.capacity


    # Size of queue
    def size(self):
        return len(self.queue)


    # Display queue
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue elements:", self.queue)


q = Queue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("Front element:", q.front())
print("Dequeued element:", q.dequeue())

q.display()
print("Queue size:", q.size())

```
---
