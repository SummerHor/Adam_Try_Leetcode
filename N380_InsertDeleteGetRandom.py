import random


class RandomizedSet:
    def __init__(self):
        self.hashMap = set()

    def insert(self, val: int) -> bool:
        if val not in self.hashMap:
            self.hashMap.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.hashMap:
            self.hashMap.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.hashMap))
