#Ejercicio 4
class Factura:
    def __init__(self, importe: float):
        self.importe = importe

    def imprimir(self):
        raise NotImplementedError("Implementar en subclase")


class FacturaA(Factura):
    """IVA Responsable"""
    def imprimir(self):
        print(f"FACTURA A  |  IVA Responsable")
        print(f"Total: ${self.importe:.2f}")


class FacturaB(Factura):
    """IVA No Inscripto"""
    def imprimir(self):
        print(f"FACTURA B  |  IVA No Inscripto")
        print(f"Total: ${self.importe:.2f}")


class FacturaC(Factura):
    """IVA Exento"""
    def imprimir(self):
        print(f"FACTURA C  |  IVA Exento")
        print(f"Total: ${self.importe:.2f}")


class FacturaFactory:
    _tipos = {
        "responsable":   FacturaA,
        "no_inscripto":  FacturaB,
        "exento":        FacturaC,
    }

    @staticmethod
    def crear(condicion: str, importe: float) -> Factura:
        clase = FacturaFactory._tipos.get(condicion.lower())
        if clase is None:
            raise ValueError(f"Condición impositiva desconocida: '{condicion}'")
        return clase(importe)



for condicion in ["responsable", "no_inscripto", "exento"]:
    f = FacturaFactory.crear(condicion, 1500.00)
    f.imprimir()
    print()