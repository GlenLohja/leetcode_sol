class RandomizedSet:

    def __init__(self):
        self.elements = {}
        self.list = []

    def insert(self, val: int) -> bool:
        res = val not in self.elements
        if res:
            self.elements[val] = len(self.list)
            self.list.append(val)
        return res

    def remove(self, val: int) -> bool:

        res = val in self.elements
        if res:
            indx = self.elements[val]
            self.list[indx] = self.list[-1]
            self.elements[self.list[-1]] = indx
            self.list.pop()
            del self.elements[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.list)
