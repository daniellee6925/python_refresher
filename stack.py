"""
LIFO: last in first out
push/pop: O(1)
search element by value O(n)

stk = deque()
"""

from collections import deque


class Stack:
    def __init__(self) -> None:
        self.container = deque()

    def push(self, value):
        self.container.append(value)  # adds a new element to the stack

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]  # get last element of stack (doesn't remove)

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def reverse_string(string):
    stack = Stack()
    for c in string:
        stack.push(c)

    output = ""
    while not stack.is_empty():
        output += stack.pop()
    return output


def is_match(ch1, ch2):
    match_dict = {")": "(", "]": "[", "}": "{"}
    return match_dict[ch1] == ch2


def is_balanced(string):
    stack = Stack()
    for c in string:
        if c == "(" or c == "{" or c == "[":
            stack.push(c)
        if c == ")" or c == "}" or c == "]":
            if stack.size() == 0:
                return False
            if not is_match(c, stack.pop()):
                return False
    return stack.size() == 0


if __name__ == "__main__":
    print(reverse_string("We will conquere COVID-19"))
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
