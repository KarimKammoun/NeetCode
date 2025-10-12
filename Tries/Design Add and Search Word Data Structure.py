class node:
    def __init__(self, val, l=None):
        if l is None:
            l = []
        self.val = val
        self.l = l
        self.end = False  


class WordDictionary:

    def __init__(self):
        self.root = node('0', [])

        
    def addWord(self, word: str, root=None) -> None:
        if root is None:
            root = self.root

        if word == "":
            root.end = True
            return

        test = False
        for i in root.l:
            if i.val == word[0]:
                self.addWord(word[1:], i)
                test = True
                break

        if not test:
            new_node = node(word[0], [])
            root.l.append(new_node)
            self.addWord(word[1:], new_node)
        

    def search(self, word: str,root=None) -> bool:
        if root is None:
            root = self.root

        if word == "":
            return root.end

        for i in root.l:
            if i.val == word[0] or word[0]==".":
                test= self.search(word[1:], i)
                if test==True:
                    return True
        return False
        
