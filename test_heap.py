from heap import get_leaf_node_values, Node, max_heapify, satisfies_heap_property, build_heap


class TestHeapFunctions:
    def test_get_leaf_node_values(self):
        input = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        leaf_node_values = get_leaf_node_values(input)
        assert leaf_node_values == [9, 3, 2, 4, 1]

    def test_max_heapify(self):
        values = list(range(20))
        max_heapify(values)
        assert values == [19, 17, 18, 15, 16, 11, 13, 3, 14, 9, 10, 2, 5, 6, 12, 0, 1, 7, 8, 4]

    def test_not_satifies_heap_property(self):
        totally_not_heapified = list(range(20))
        assert not satisfies_heap_property(totally_not_heapified)

    def test_satifies_heap_property(self):
        heapified = [19, 17, 18, 15, 16, 11, 13, 3, 14, 9, 10, 2, 5, 6, 12, 0, 1, 7, 8, 4]
        assert satisfies_heap_property(heapified)

    def test_build_heap(self):
        root_node = build_heap(list(range(21)))
        assert root_node.value == 20