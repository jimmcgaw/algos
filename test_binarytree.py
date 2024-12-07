from binarytree import create_balanced_binary_tree, create_binary_tree, create_sorted_binary_tree, Node, traverse_node, get_height, is_balanced, is_perfect


class TestNode:
    def test_node(self):
        # A node with >0 children is not leaf node.
        right = Node(3)
        left = Node(1)
        node = Node(2, left=left, right=right)
        assert not node.is_leaf

        node.left = None
        assert not node.is_leaf

    def test_leaf_node(self):
        # A node with no children is leaf node.
        node = Node(3)
        assert node.is_leaf


class TestBinaryTree:
    INPUT = [3,5,2,1,4,6,7,8,9,10,11,12,13,14]

    def test_empty_list(self):
        assert create_binary_tree([]) is None

    def test_sorted_binary_tree(self):
        tree = create_sorted_binary_tree(self.INPUT)

    def test_traverse_sorted_binary_tree(self):
        tree = create_sorted_binary_tree(self.INPUT)
        vals = traverse_node(tree)
        height = get_height(tree)

    def test_traverse_node(self):
        node = Node(
            value=2,
            left=Node(1),
            right=Node(3)
        )
        assert traverse_node(node) == [1,2,3]


class TestBalancedBinaryTree:
    def test_create_balanced_bintree_len_2(self):
        node = create_balanced_binary_tree([4,5])
        assert node.value == 5
        assert node.left is not None
        assert node.left.value == 4
        assert node.right is None

    def test_create_balanced_bintree_len_2_unordered(self):
        node = create_balanced_binary_tree([5, 4])
        assert node.value == 5
        assert node.left is not None
        assert node.left.value == 4
        assert node.right is None

    def test_create_balanced_binary_tree(self):
        values = list(range(1, 2**5-3))
        root = create_balanced_binary_tree(values)
        assert get_height(root) == 5
        assert traverse_node(root) == values


class TestPerfectBinaryTree:
    def test_create_imperfect_binary_tree(self):
        values = list(range(1, 2**5-3))
        root = create_balanced_binary_tree(values)
        assert get_height(root) == 5
        assert not is_perfect(root)

    def test_create_perfect_binary_tree(self):
        values = list(range(1, 2**5))
        root = create_balanced_binary_tree(values)
        assert get_height(root) == 5
        assert is_perfect(root)