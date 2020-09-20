class Cargo:
    def __init__(self, name, weight=10):
        self.name = name
        self.weight = weight

    def __str__(self):
        return self.name
