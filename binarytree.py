from typing import Optional

class Node:
    left: Optional["Node"]
    right: Optional["Node"]

    def __init__(self, value: any, left: "Node" = None, right: "Node" = None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        viz = f"<Node val={self.value} "
        if self.left:
            viz += f"left={self.left.value} "
        if self.right:
            viz += f"right={self.right.value} "
        viz += "/>"
        return viz
    
    @property
    def is_leaf(self):
        return self.left is None and self.right is None


input = [3,5,2,1,4,6,7,8,9,10,11,12,13,14]


# indicies:
# root: 0, 1, 2
# root left: 1, 3, 4
# root right: 2, 5, 6
# root left left: 3, 7, 8
# root left right: 4, 9, 10
# root right left: 5, 11, 12
# root right right: 6, 13

# Pattern: for node at index N, children are at indices 2*N+1 and 2*N+2

def create_binary_tree(values: list[any]) -> Optional[Node]:
    if not len(values):
        return None
    
    def _create_subtree(index: int = 0):
        if index > len(values) or values[index] is None:
            return None
        
        left_index = index * 2 + 1
        right_index = index * 2 + 2
        left = _create_subtree(index=left_index)
        right = _create_subtree(index=right_index)
        return Node(values[index], left=left, right=right)

    return _create_subtree(index=0)


def create_sorted_binary_tree(values: list[any]):
    if not len(values):
        return None
    
    def _insert_node(node: Node, value: any):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                _insert_node(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                _insert_node(node.right, value)
    
    root = Node(values[0])
    for index in range(1, len(values)):
        value = values[index]
        _insert_node(root, value)

    return root


def traverse_node(node: Node):
    if not isinstance(node, Node):
        raise ValueError(
            f'{node} must be an instance of Node class'
        )
    
    if not node:
        return []
    
    vals = []

    if node.left is not None:
        vals.extend(traverse_node(node.left))
    vals.append(node.value)
    if node.right is not None:
        vals.extend(traverse_node(node.right))

    return vals


def get_height(node: Node, height: int = 0):
    """Recursively computes the height of a binary tree, given a parent node."""
    if not node:
        return 0
    
    # base case - leaf node, just adds 1 to height
    if node.is_leaf:
        return height + 1
    
    # recursive case - height is max of left and right subtrees
    left_height = get_height(node.left, height=height+1)
    right_height = get_height(node.right, height=height+1)
    return max(left_height, right_height)


def is_balanced(node: Node):
    if not node:
        return True
    
    if node.is_leaf:
        return True
    
    left_height = get_height(node.left)
    right_height = get_height(node.right)
    return not abs(left_height - right_height) > 1


# TODO: does this detect a perfect tree or merely a full one?
def is_perfect(node: Node):
    if not node:
        return False
    
    if node.is_leaf:
        return True
    
    if node.left is not None and node.right is not None:
        return (
            is_perfect(node.left) and is_perfect(node.right)
        )
    
    return False


def create_balanced_binary_tree(values: list[any]):
    if not values:
        return None
    
    # base cases
    if len(values) == 1:
        return Node(values[0])
    
    if len(values) == 2:
        val0, val1 = sorted(values)
        return Node(val1, left=Node(value=val0))
    
    # recursive case
    mid_index = len(values) // 2
    mid_value = values[mid_index]

    left_values = values[:mid_index]
    right_values = values[mid_index+1:]

    node = Node(mid_value)
    if left_values:
        node.left = create_balanced_binary_tree(left_values)
    if right_values:
        node.right = create_balanced_binary_tree(right_values)

    return node
        
    


