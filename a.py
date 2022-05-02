class A:
    def __init__():
        pass
class Test(A):
    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age
a = Test(age = 4, name ="Hello")
print(a.age)
print(a.name)