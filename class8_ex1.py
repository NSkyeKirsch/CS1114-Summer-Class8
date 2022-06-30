# class topic: recursion

# __len__(self): returns length of the object (if appropriate)
# len(list)
# __add__(self, other): add two items of the same type together
# __sub__(self, other):
# __mul__(self, other): multiplication
# __div__(self, other): divide
# __floordiv__(self, other):
# __pow__(self, other):
# __eq__(self, other):
# __lt__(self, other):

# collection class: stuff goes in it

class Value:  # represents a value that is stored
    def __init__(self, num):
        self.value = num

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        result = self.value + other.value
        return Value(result)

    def __pow__(self, other):


v1 = Value("Hello")
v2 = Value(4)
v3 = Value(2)
result = v2 + v3  # v2.__add__(v3)
print(type(result), result)

print(v2 ** v3)  # v2.__pow__(v3)
print(v3 ** v2)

