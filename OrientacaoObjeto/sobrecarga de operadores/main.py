class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'<class "Retangulo({self.x}, {self.y})">'

    def get_area(self):
        return self.x * self.y

    def __add__(self, other):
        # self representa o p1 e other p2
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)

    # menor que
    def __lt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        return True if a1 < a2 else False

    # maior que
    def __gt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        return True if a1 > a2 else False

    # igualdade
    def __eq__(self, other):
        return True if (self.x == other.x and self.y == other.y) else False


r1 = Retangulo(10, 20)
r2 = Retangulo(30, 50)
print(r1)

r3 = r1 + r2
r4 = Retangulo(40, 70)

print(r3)

print(r3 > r1)
print(r3 < r1)
print(r3 == r4)
print(r2 == r1)

