class TrieNode(object):

    def __init__(self):
        self.children = [None]*26
        self.isLastChar = False

class Trie(object):
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):
        startingPoint = self.root
        length = len(word)
        for char in range(length):
            index = self._charToIndex(word[char])
            if not startingPoint.children[index]:
                startingPoint.children[index] = self.getNode()
                print("Node created for : " +str(char))
            startingPoint = startingPoint.children[index]

        startingPoint.isLastchar = True
l = input('enter: ')
t = Trie()
a = 'abc'
b = 'ade'
#b = 'ade'
t.insert(a)
t.insert(b)
