# Ejercicio 5

class Avion(object):
    def __init__(self, body, turbina1, turbina2, ala1, ala2, tren_aterrizaje):
        self.body            = body
        self.turbina1        = turbina1
        self.turbina2        = turbina2
        self.ala1            = ala1
        self.ala2            = ala2
        self.tren_aterrizaje = tren_aterrizaje


class AvionBuilder(object):
    def __init__(self, body):
        self.body            = body
        self.turbina1        = None
        self.turbina2        = None
        self.ala1            = None
        self.ala2            = None
        self.tren_aterrizaje = None

    def build(self):
        return Avion(self.body, self.turbina1, self.turbina2,
                     self.ala1, self.ala2, self.tren_aterrizaje)


class AvionComercialBuilder(object):
    def __init__(self):
        self.body            = 'Fuselaje comercial'
        self.turbina1        = 'Turbina izquierda'
        self.turbina2        = 'Turbina derecha'
        self.ala1            = 'Ala izquierda'
        self.ala2            = 'Ala derecha'
        self.tren_aterrizaje = 'Tren retráctil'

    def build(self):
        return Avion(self.body, self.turbina1, self.turbina2,
                     self.ala1, self.ala2, self.tren_aterrizaje)


a = AvionBuilder('Fuselaje liviano')
a.turbina1        = 'Turbina única'
a.ala1            = 'Ala izquierda'
a.ala2            = 'Ala derecha'
a.tren_aterrizaje = 'Tren fijo'
a.build()
print(a.body, a.turbina1, a.ala1, a.ala2, a.tren_aterrizaje)

b = AvionComercialBuilder()
b.build()
print(b.body, b.turbina1, b.turbina2, b.ala1, b.ala2, b.tren_aterrizaje)

c = Avion('Fuselaje estándar',
          'Turbina izquierda', 'Turbina derecha',
          'Ala izquierda', 'Ala derecha',
          'Tren retráctil')
print(c.body, c.turbina1, c.turbina2, c.ala1, c.ala2, c.tren_aterrizaje)