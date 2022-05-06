class A:
    def __init__(self): pass

    def test(self):
        print(B.att)
        print(C.att)

class B:
    att = 1
    def __init__(self): pass

class C:
    
    att = 1
    def __init__(self):
        pass


a = 16
obj = A()
obj.test()