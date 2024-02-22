class Gene:

    def __init__(self, value: any, low_boundry: any = None, high_boundry: any = None):

        self.low_boundry = low_boundry
        self.high_boundry = high_boundry
        self.value = value

    def get_value(self):

        return self.value

    def set_value(self, value):

        self.value = value

    def get_boundries(self):

        return (self.low_boundry, self.high_boundry)

    # str and repr for this gene
    def __str__(self):
        return f"Gene: {self.value}"

    def __repr__(self):
        return f"Gene: {self.value}"

    def __eq__(self, other):
        if not isinstance(other, Gene):
            return NotImplemented
        return self.value == other.value
