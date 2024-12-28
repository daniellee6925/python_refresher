"""
first in first out FIFO
"""

from collections import deque
import time
import threading


class Queue:
    def __init__(self) -> None:
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


food_order = Queue()


def place_order(orders):
    for order in orders:
        print("Placing order for:", order)
        food_order.enqueue(order)
        time.sleep(0.5)


def serve_order():
    time.sleep(1)
    while True:
        x = food_order.dequeue()
        print("Now Serving: ", x)
        time.sleep(2)


if __name__ == "__main__":
    orders = ["pizza", "samosa", "pasta", "fries", "burger"]
    # multithreading
    t1 = threading.Thread(target=place_order, args=(orders,))
    t2 = threading.Thread(target=serve_order)
    t1.start()
    t2.start()
