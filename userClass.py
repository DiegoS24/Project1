# import string

class User:
    def __init__(self, name):
        self.name = name
        self.val = 0

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setVal(self, val):
        self.val = val

    def getVal(self):
        return self.val
