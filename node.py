class Node:
    def __init__(self, token, children=None, leaf=None):
        self.token = token
        if children:
            self.children = children
        else:
            self.children = []
        self.leaf = leaf
        if None in self.children:
            print(f'Alerta!!! {token}')

    def printAST(self, indent):
        print((indent * '  '), self.token, f'({self.leaf})')
        if self.children:
            for child in self.children:
                # print(((indent + 1) * '  '), self.leaf[0])
                child.printAST(indent + 1)