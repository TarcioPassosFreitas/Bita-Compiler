class SynthaticNode:
    def __init__(self, production: str):
        self.production = production
        self.count = 0

    def add(self, param):
        self.count += 1

    def is_not_empty(self) -> bool:
        return self.count != 0
