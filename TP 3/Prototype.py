# Ejercicio 6 

class Note(object):

    def __init__(self, fraction):
        self.fraction = fraction

    def get(self):
        return self.fraction

    def clone(self):
        return Note(self.fraction)



x = Note(10)
print("Valor almacenado en (x) fraction %d" % (x.get()))

a = x.clone()
print("Valor almacenado en (a) fraction %d" % (a.get()))

b = a.clone()
print("Valor almacenado en (b) fraction %d" % (b.get()))

print("¿x es a?", x is a)
print("¿a es b?", a is b)