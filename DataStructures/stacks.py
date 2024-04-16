from typing import Optional

class Stack:
    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        self.size = 0
        self.s = [-1] * capacity

    def top(self) -> Optional[int]:
        if self.size == 0:
            print("Stack is empty")
            return None
        else:
            return self.s[self.size - 1]

    def pop(self) -> Optional[int]:
        if self.size == 0:
            print("Underflow")
            return None
        else:
            val = self.s[self.size - 1]
            self.s[self.size - 1] = -1
            self.size -= 1
            return val

    def push(self, val: int):
        if self.size >= self.capacity:
            print("Stack Overflow")
        else:
            self.s[self.size] = val
            self.size += 1

    def display(self):
        print(self.s[:self.size])

if __name__ == "__main__":
    my_stack = Stack()

    for i in range(5):
        my_stack.push(i)

    my_stack.display()

    v1 = my_stack.pop()
    print(v1)
    
    print(my_stack.top())

    my_stack.pop()
    my_stack.push(15)
    my_stack.display()
    my_stack.pop()
    my_stack.pop()
    my_stack.display()
    my_stack.pop()
    my_stack.pop()
    my_stack.display()

    my_stack.pop()

    for i in range(12):
        my_stack.push(i)

    my_stack.display()
    
