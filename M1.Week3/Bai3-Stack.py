class MyStack:
    def __init__(self, capacity):
        self._capacity = capacity
        self._stack = []

    # push(value) add thêm value vào trong stack
    def push(self, item):
        self._stack.append(item)

    # pop loại bỏ top element và trả về giá trị đó
    def pop(self):
        return self._stack.pop()

    # lấy giá trị top element hiện tại của stack, nhưng không loại bỏ giá trị đó
    def top(self):
        return self._stack[-1]

    def is_empty(self):
        print(f"độ lớn của stack: {len(self._stack)}")
        return len(self._stack) == 0

    def is_full(self):
        return len(self._stack) == self._capacity


stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())

#câu 9
print('Kết quả câu 9:')

stack2 = MyStack(capacity=5)
stack2.push(1)
assert stack2.is_full() == False
stack2.push(2)
print(stack2.is_full())

#câu 10

print('Kết quả câu 10:')
stack3 = MyStack(capacity=5)
stack3.push(1)
assert stack3.is_full() == False
stack3.push(2)
print(stack3.top())