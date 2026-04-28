#Ejercicio 3
class Hamburguesa:
    def __init__(self):
        self.entrega   = "mostrador"
        self.direccion = None

    def describir(self):
        print(f" Hamburguesa | Entrega: {self.entrega.upper()}")
        if self.direccion:
            print(f"   Dirección de entrega: {self.direccion}")


class HamburguesaBuilder:
    def __init__(self):
        self._hamburguesa = Hamburguesa()

    def set_entrega(self, tipo: str):
        """tipo: 'mostrador' | 'retiro' | 'delivery'"""
        self._hamburguesa.entrega = tipo
        return self          

    def set_direccion(self, direccion: str):
        self._hamburguesa.direccion = direccion
        return self

    def build(self) -> Hamburguesa:
        producto = self._hamburguesa
        self._hamburguesa = Hamburguesa()
        return producto



builder = HamburguesaBuilder()

h1 = builder.set_entrega("mostrador").build()
h1.describir()


h2 = builder.set_entrega("retiro").build()
h2.describir()


h3 = builder.set_entrega("delivery").set_direccion("Av. San Martín 123").build()
h3.describir()
