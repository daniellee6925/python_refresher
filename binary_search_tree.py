"""
does set (only returns non-duplicate elements)
does sorting : in ordeer traversal
left node always less than root
right node always greater than root
"""


class BinarySearchTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in left subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []
        # in order -> left -> root -> right

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        # post order: left  -> right -> root

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()
        # visit base node
        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = []
        # pre order: root -> left -> right

        # visit base node
        elements.append(self.data)

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True

        elif val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        # node data matches value
        else:
            # if no child, delete node
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val  # set deleted node to minimum value
            self.right = self.right.delete(min_val)  # delete dupilicate node

        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == "__main__":
    numbers = [17, 4, 2, 20, 9, 23, 18, 21]
    numbers_tree = build_tree(numbers)
    numbers_tree.delete(21)
    print(numbers_tree.in_order_traversal())
