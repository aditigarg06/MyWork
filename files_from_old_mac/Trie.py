class TrieNode(object):
    def __init__(self):
        self.children = []
        for i in range(0, 26):
            self.children.append(None)
        self.isWord = 1
        self.isPrefix = 0
        self.parent = None


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        temp_node = self.root
        temp_word = word
        firstLetter = temp_word[0]
        pos = abs(ord(firstLetter) - 97)
        while temp_node.children[pos] != None:
            temp_node = temp_node.children[pos]
            temp_node.isWord = 0
            temp_node.isPrefix = temp_node.isPrefix + 1
            temp_word = temp_word[1:]
            firstLetter = temp_word[0]
            pos = abs(ord(firstLetter) - 97)

        if len(temp_word) > 0:
            for c in temp_word:
                firstLetter = temp_word[0]
                pos = abs(ord(firstLetter) - 97)
                temp_node.children[pos] = TrieNode()
                temp_node.children[pos].parent = temp_node
                temp_node = temp_node.children[pos]

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        temp_node = self.root
        temp_word = word
        firstLetter = temp_word[0]
        pos = abs(ord(firstLetter) - 97)
        while temp_node.children[pos] != None:
            temp_node = temp_node.children[pos]
            temp_node.isWord = 0
            temp_node.isPrefix = temp_node.isPrefix + 1
            temp_word = temp_word[1:]
            firstLetter = temp_word[0]
            pos = abs(ord(firstLetter) - 97)

        if len(temp_word) > 0:
            return False
        else:
            return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        temp_node = self.root
        temp_word = word
        firstLetter = temp_word[0]
        pos = abs(ord(firstLetter) - 97)
        while temp_node.isWord != 1:
            temp_node = temp_node.children[pos]
            temp_node.isWord = 0
            temp_node.isPrefix = temp_node.isPrefix + 1
            temp_word = temp_word[1:]
            firstLetter = temp_word[0]
            pos = abs(ord(firstLetter) - 97)

        if len(temp_word) > 0:
            return False
        else:
            return True

            # Your Trie object will be instantiated and called as such:
            # trie = Trie()
            # trie.insert("somestring")
            # trie.search("key")