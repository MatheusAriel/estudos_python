class A:
    vc = 123

    def __init__(self):
        self.vc = 98090

a1 = A()
a2 = A()

A.vc='ALTERADO'
print(a1.vc)
a1.vc = 3456
print(a1.__dict__)
print(a2.__dict__)


print(a2.vc)
print(A.vc)

print()

A.vc = 321
print(a1.vc)
print(a2.vc)
print(A.vc)
