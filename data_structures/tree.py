class TreeNode:
    def __init__(self, name, designation) -> None:
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, type):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "I__" if self.parent else ""

        if type == "name":
            print(prefix + self.name)

        if type == "designation":
            print(prefix + self.designation)

        if type == "both":
            print(prefix + self.name + " (" + self.designation + ")")

        if self.children:
            for child in self.children:
                child.print_tree(type)


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Galaxy"))
    cellphone.add_child(TreeNode("Google Pixel"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    return root


def build_management_tree():
    root = TreeNode("Audrey", "CEO")

    CTO = TreeNode("Alex", "CTO")
    Infra_head = TreeNode("Tom", "Infrastructure Head")
    Infra_head.add_child(TreeNode("Austin", "Cloud Manager"))
    Infra_head.add_child(TreeNode("Albert", "App Manager"))
    App_head = TreeNode("Taishi", "Application Head")
    CTO.add_child(Infra_head)
    CTO.add_child(App_head)

    HR = TreeNode("Kat", "HR Head")
    HR.add_child(TreeNode("Hannah", "Recruitment Manager"))
    HR.add_child(TreeNode("Eric", "Policy Manager"))

    root.add_child(CTO)
    root.add_child(HR)

    return root


if __name__ == "__main__":
    root_node = build_management_tree()
    root_node.print_tree("name")  # prints only name hierarchy
    root_node.print_tree("designation")  # prints only designation hierarchy
    root_node.print_tree("both")  # prints both (name and designation) hierarchy
