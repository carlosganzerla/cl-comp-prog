def check_binary_search_tree_(root):
    def loop(node, max_value, min_value):
        if not node:
            return True
        if (node.data >= max_value or
            node.data <= min_value or
            node.left and node.left.data >= node.data or
            node.right and node.right.data <= node.data or
            node.left and node.right and node.left.data >= node.right.data):
            return False

        return (loop(node.left, node.data, min_value) and
                loop(node.right, max_value, node.data))
    return loop(root, 1000000000, -1)
