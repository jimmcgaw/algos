from typing import Optional


def get_leaf_node_values(heap_vals: list[float]):
    # any index n with children has values at indices 2*n+1 and 2*n=2
    # take last index and invert to find lower bound
    last_index = len(heap_vals)-1
    last_parent_index = (last_index-2)//2+1
    first_leaf_index = last_parent_index+1
    return heap_vals[first_leaf_index:len(heap_vals)]


class Node:
    left: Optional["Node"]
    right: Optional["Node"]
    # track parent node so we can run heapify without a parent pointer
    parent: Optional["Node"]
    # Python needs a generic numeric type
    value: float

    def __init__(self, value, left: "Node" = None, right: "Node" = None, parent: "Node" = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    @property
    def is_leaf(self) -> bool:
        return self.left is None and self.right is None


def max_heapify(values: list[float]):
    """Given a list, run max-heapify on the list, recursively on child nodes where swaps happen.
    Modifies the list in-place.
    """
    def _max_heapify(index: int = 0):
        for index in range(last_parent_index, -1, -1):
            val = values[index]
            # print(f"Index {index} with value {val}")
            left_child_index = 2 * index + 1
            if left_child_index < len(values):
                left_child_val = values[left_child_index]
                # print(f"Left child {left_child_index} with value {left_child_val}")
                if val < left_child_val:
                    # print(f"Swapping {val} and {left_child_val}")
                    values[index], values[left_child_index] = values[left_child_index], values[index]
                    _max_heapify(index=left_child_index)
            right_child_index = 2 * index + 2
            if right_child_index < len(values):
                right_child_val = values[right_child_index]
                # print(f"Right child {right_child_index} with value {right_child_val}")
                if val < right_child_val:
                    values[index], values[right_child_index] = values[right_child_index], values[index]
                    _max_heapify(index=right_child_index)

    last_index = len(values)-1
    last_parent_index = (last_index-2)//2+1
    _max_heapify(index=last_parent_index)


def satisfies_heap_property(values: list[float]) -> bool:
    """Given a list of values, returns True is list satisfies the max-heap property"""
    for index in range(len(values)):
        value = values[index]
        left_child_index = 2*index+1
        if left_child_index < len(values):
            left_child_value = values[2*index+1]
            if left_child_value > value:
                return False
        right_child_index = 2*index+2
        if right_child_index < len(values):
            right_child_value = values[2*index+2]
            if right_child_value > value:
                return False
    return True
    

def build_heap(values: list[float]):
    """Given a list of values, runs max-heapify on the list and builds a binary max heap.
    Returns the root node of the tree.
    """
    max_heapify(values)

    def _build_subtree(index: int = 0, parent: "Node" = None):
        if index >= len(values) or values[index] is None:
            return None

        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        node = Node(value=values[index], parent=parent)
        node.left = _build_subtree(index=left_child_index, parent=node)
        node.right = _build_subtree(index=right_child_index, parent=node)
        return node

    return _build_subtree(index=0)
