class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = "RED"


class RedBlackTree:
    def __init__(self):
        self.nil = Node(None)
        self.root = self.nil

    def insert(self, value):
        new_node = Node(value)
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.color = "RED"

        current_node = self.root
        parent_node = None

        while current_node != self.nil:
            parent_node = current_node
            if new_node.value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        new_node.parent = parent_node

        if parent_node is None:
            self.root = new_node
        elif new_node.value < parent_node.value:
            parent_node.left = new_node
        else:
            parent_node.right = new_node

        if new_node.parent is None:
            new_node.color = "BLACK"
            return

        if new_node.parent.parent is None:
            return

        self.rebalanse(new_node)

    def rebalanse(self, node):
        while node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle_node = node.parent.parent.right

                if uncle_node.color == "RED":
                    node.parent.color = "BLACK"
                    uncle_node.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)

                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.rotate_right(node.parent.parent)
            else:
                uncle_node = node.parent.parent.left

                if uncle_node.color == "RED":
                    node.parent.color = "BLACK"
                    uncle_node.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)

                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.rotate_left(node.parent.parent)

        self.root.color = "BLACK"

    def rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left

        if right_child.left != self.nil:
            right_child.left.parent = node

        right_child.parent = node.parent

        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right

        if left_child.right != self.nil:
            left_child.right.parent = node

        left_child.parent = node.parent

        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        left_child.right = node
        node.parent = left_child
