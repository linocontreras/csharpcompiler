class Node:
    def __init__(self, token, children=None, leaf=None):
        self.token = token
        if children:
            self.children = children #list(filter(lambda x: x is not None, children))
        else:
            self.children = []
        self.leaf = leaf

    def printAST(self, indent=0):
        print((indent * '  '), self.token, f'({self.leaf})')
        if self.children:
            for child in self.children:
                # print(((indent + 1) * '  '), self.leaf[0])
                child.printAST(indent + 1)