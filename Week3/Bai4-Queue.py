class MyQueue():
    def __init__(self, capacity):
        self._queue = []
        self._capacity = capacity

    # add thêm value vào trong queue
    def enqueue(self, value):
        self._queue.append(value)

    # loại bỏ first element và trả về giá trị đó
    def dequeue(self):
        return self._queue.pop(0)

    # lấy giá trị first element hiện tại của queue, nhưng không loại bỏ giá trị đó
    def front(self):
        return self._queue[0]

    # kiểm tra queue có rỗng không
    def is_empty(self):
        return len(self._queue) == 0

    # kiểm tra queue có đầy không
    def is_full(self):
        return len(self._queue) == self._capacity


queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())

# câu 11

print('Kết quả câu 11:')
queue2 = MyQueue(capacity=5)
queue2.enqueue(1)
assert queue2.is_full() == False
queue2.enqueue(2)
print(queue2.is_full())

# Câu 12:

print('Kết quả câu 12:')
queue3 = MyQueue(capacity=5)
queue3.enqueue(1)
assert queue3.is_full() == False
queue3.enqueue(2)
print(queue3.front())
