class node:
    def __init__(self, val, l=None):
        if l is None:
            l = []
        self.val = val
        self.l = l
        self.end = False  


class PrefixTree:

    def __init__(self):
        self.root = node('0', [])

    def insert(self, word: str, root=None) -> None:
        if root is None:
            root = self.root

        if word == "":
            root.end = True
            return

        test = False
        for i in root.l:
            if i.val == word[0]:
                self.insert(word[1:], i)
                test = True
                break

        if not test:
            new_node = node(word[0], [])
            root.l.append(new_node)
            self.insert(word[1:], new_node)

    def search(self, word: str, root=None) -> bool:
        if root is None:
            root = self.root

        if word == "":
            return root.end

        for i in root.l:
            if i.val == word[0]:
                return self.search(word[1:], i)

        return False

    def startsWith(self, prefix: str, root=None) -> bool:
        if root is None:
            root = self.root

        if prefix == "":
            return True

        for i in root.l:
            if i.val == prefix[0]:
                return self.startsWith(prefix[1:], i)

        return False
