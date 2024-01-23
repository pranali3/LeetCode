from collections import defaultdict


class FileSystem:
    def __init__(self):
        # SC: O(n)
        self.paths = defaultdict()

    def createPath(self, path: str, value: int) -> bool:
        # TC: O(n)
        if path in self.paths:
            return False
        if path.count("/") > 1:
            parentPath = "/".join(path.split("/")[:-1])
            if parentPath not in self.paths:
                return False
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        # TC: O(1)
        if path in self.paths:
            return self.paths[path]
        return -1

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
