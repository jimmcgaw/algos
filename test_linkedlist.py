from linkedlist import LinkedList, Node


class TestNode:
    def test_node_data(self):
        node = Node(data=1)
        node.next = Node(data=2)

        assert node.next.data == 2


class TestLinkedList:
    def test_create_list(self):
        head = Node(data=20)
        linked = LinkedList(head=head)
        assert linked.head.data == 20

    def test_insert_at_head(self):
        head = Node(data=20)
        linked = LinkedList(head=head)
        assert linked.traverse() == [20]

        linked.insert_at_head(
            Node(data=10)
        )
        assert linked.traverse() == [10, 20]

    def test_insert_at_head_empty_list(self):
        empty = LinkedList()
        empty.insert_at_head(
            Node(data=10)
        )
        assert empty.traverse() == [10]

    def test_insert_at_tail(self):
        linked = LinkedList(
            head=Node(data=20)
        )
        assert linked.traverse() == [20]
        linked.insert_at_tail(
            Node(data=30)
        )
        assert linked.traverse() == [20, 30]

    def test_insert_at_tail_empty_list(self):
        empty = LinkedList()
        empty.insert_at_tail(
            Node(data=10)
        )
        assert empty.traverse() == [10]

    def test_insert_before(self):
        linked = LinkedList(
            head=Node(data=10)
        )
        linked.insert_at_tail(node=Node(data=20))
        linked.insert_at_tail(node=Node(data=40))
        linked.insert_at_tail(node=Node(data=50))
        assert linked.traverse() == [10, 20, 40, 50]
        linked.insert_before(
            node=Node(data=30), data=40
        )
        assert linked.traverse() == [10, 20, 30, 40, 50]

    def test_insert_after(self):
        linked = LinkedList(
            head=Node(data=10)
        )
        linked.insert_at_tail(node=Node(data=20))
        linked.insert_at_tail(node=Node(data=40))
        linked.insert_at_tail(node=Node(data=50))
        assert linked.traverse() == [10, 20, 40, 50]
        assert linked.insert_after(
            node=Node(data=30), data=20
        )
        assert linked.traverse() == [10, 20, 30, 40, 50]

    def test_insert_after_missing_data(self):
        linked = LinkedList(
            head=Node(data=10)
        )
        linked.insert_at_tail(node=Node(data=20))
        linked.insert_at_tail(node=Node(data=40))
        assert not linked.insert_after(
            node=Node(data=35),
            data=30
        )

    def test_search_existing_element(self):
        linked = LinkedList(
            head=Node(data=10)
        )
        linked.insert_at_tail(node=Node(data=20))
        linked.insert_at_tail(node=Node(data=30))
        linked.insert_at_tail(node=Node(data=40))
        node = linked.search(data=30)
        assert node is not None
        assert node.data == 30

    def test_search_nonexistent_element(self):
        linked = LinkedList(
            head=Node(data=10)
        )
        linked.insert_at_tail(node=Node(data=20))
        linked.insert_at_tail(node=Node(data=30))
        linked.insert_at_tail(node=Node(data=40))
        assert linked.search(data=500) is None

    def test_traverse(self):
        linked = LinkedList(
            head=Node(data=10)
        )
        linked.insert_after(node=Node(data=20), data=10)
        linked.insert_after(node=Node(data=30), data=20)
        linked.insert_after(node=Node(data=40), data=30)
        assert linked.traverse() == [10,20,30,40]

    def test_reverse(self):
        linked = LinkedList(
            head=Node(data=10)
        )
        linked.insert_after(node=Node(data=20), data=10)
        linked.insert_after(node=Node(data=30), data=20)
        linked.insert_after(node=Node(data=40), data=30)
        assert linked.traverse() == [10,20,30,40]
        linked.reverse()
        assert linked.traverse() == [40,30,20,10]

    def test_rotate(self):
        linked = LinkedList(
            head=Node(data=10)
        )
        linked.insert_after(node=Node(data=20), data=10)
        linked.insert_after(node=Node(data=30), data=20)
        linked.insert_after(node=Node(data=40), data=30)
        assert linked.traverse() == [10,20,30,40]
        linked.rotate(k=2)
        assert linked.head.data == 30
        assert linked.traverse() == [30,40,10,20]

    def test_is_empty(self):
        linked = LinkedList()
        assert linked.is_empty()

    def test_is_not_empty(self):
        linked = LinkedList(head=Node(data=10))
        assert not linked.is_empty()

    def test_is_palindrome(self):
        linked = LinkedList(
            head=Node(data=10)
        )
        linked.insert_at_tail(node=Node(data=20))
        linked.insert_at_tail(node=Node(data=30))
        linked.insert_at_tail(node=Node(data=20))
        linked.insert_at_tail(node=Node(data=10))
        assert linked.traverse() == [10, 20, 30, 20, 10]
        assert linked.is_palindrome()

        linked.insert_at_tail(node=Node(100))
        assert not linked.is_palindrome()

    def test_mth_to_last_element(self):
        linked = LinkedList()
        for i in range(1, 31):
            linked.insert_at_tail(node=Node(data=i))
        node: Node = linked.get_mth_to_last_element(5)
        assert node.data == 26

    def test_merge_sorted_lists(self):
        linked = LinkedList(
            head=Node(data=10)
        )
        linked.insert_at_tail(node=Node(data=20))
        linked.insert_at_tail(node=Node(data=30))

        other = LinkedList(head=Node(data=5))
        other.insert_at_tail(node=Node(data=15))
        other.insert_at_tail(node=Node(data=25))
        other.insert_at_tail(node=Node(data=35))

        merged: LinkedList = linked.merge(other)
        assert merged.traverse() == [5,10,15,20,25,30,35]