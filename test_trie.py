from trie import Trie, TrieNode


class TestTrieNode:
    def test_trie_node_init(self):
        node = TrieNode()
        assert node.children == {}
        assert not node.is_end


class TestTrie:
    def test_build_trie(self):
        trie = Trie()
        trie.build_trie(["hello", "world", "hell", "help"])
        assert trie.root.children["h"].children["e"].children["l"].children["l"].is_end
        assert trie.root.children["w"].children["o"].children["r"].children["l"].children["d"].is_end
        assert trie.root.children["h"].children["e"].children["l"].children["p"].is_end
        assert not trie.root.children["h"].children["e"].children["l"].is_end

    def test_insert_word(self):
        trie = Trie()
        trie.insert_word("hello")
        assert not trie.root.children["h"].is_end
        assert not trie.root.children["h"].children["e"].is_end
        assert not trie.root.children["h"].children["e"].children["l"].is_end
        assert not trie.root.children["h"].children["e"].children["l"].children["l"].is_end
        assert trie.root.children["h"].children["e"].children["l"].children["l"].children["o"].is_end

    def test_search_word(self):
        trie = Trie()
        trie.build_trie(["hello", "world", "hell", "help"])
        assert trie.search_word("hello")
        assert trie.search_word("world")
        assert trie.search_word("hell")
        assert trie.search_word("help")
        assert not trie.search_word("hellp")
        assert not trie.search_word("worlds")
        assert not trie.search_word("hello world")
        assert not trie.search_word("hello world help")
        assert not trie.search_word("hello world hell")
        assert not trie.search_word("hello world help")