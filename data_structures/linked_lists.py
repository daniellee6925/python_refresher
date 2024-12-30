"""
Linked Lists
1. you don't need to pre-allocate space
2. insertion is easier and less computational
"""


class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "--->"
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("This is not a valid index")
        if index == 0:
            # python automatically does garbage collection: clears memory
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr.next:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("This is not a valid index")
        if index == 0:
            self.insert_at_begining(data)
            return
        if index == self.get_length():
            self.insert_at_end(data)
            return
        count = 0
        itr = self.head
        while itr.next:
            if count == index - 1:
                next_node = itr.next
                itr.next = Node(data, next_node)
                break
            count += 1
            itr = itr.next

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


if __name__ == "__main__":
    ll = LinkedList()
    # ll.insert_at_begining(5)
    # ll.insert_at_begining(89)
    # ll.insert_at_end(79)
    ll.insert_values(["A", "B", "C", "D"])
    ll.insert_after_value("B", "C")
    ll.remove_by_value("B")
    ll.print()
