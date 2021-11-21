
class Fractie:

    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f'Numerele noastre {self.numarator} si {self.numitor}'


numerele = Fractie(10, 20)
print(numerele.numarator, numerele.numitor)

print(numerele.__str__())


class Adi:
    def __init__(self, suma):
        self.a = suma

    def __add__(self, other):
        return self.a + other.a

    def __sub__(self, other):
        return self.a - other.a


ob1 = Adi(174)
ob2 = Adi(273)

print(ob1 + ob2)
print(ob2 - ob1)

