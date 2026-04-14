"""
Calculadora RPN (Reverse Polish Notation)

Implementa una calculadora basada en pila capaz de evaluar
expresiones matemáticas en notación polaca inversa.
"""

import math
import sys


class RPNError(Exception):
    """Excepción personalizada para errores de la calculadora RPN."""
    pass


class RPN:
    """Clase principal que gestiona la pila, memoria y evaluación."""

    def __init__(self) -> None:
        # Pila de operandos
        self.stack: list[float] = []

        # Memoria (00 a 09)
        self.mem: dict[str, float] = {f"{i:02}": 0.0 for i in range(10)}

    def push(self, value: float) -> None:
        """Agrega un valor a la pila."""
        self.stack.append(value)

    def pop(self) -> float:
        """Extrae el último valor de la pila."""
        if not self.stack:
            raise RPNError("Pila insuficiente")
        return self.stack.pop()

    def eval(self, expr: str) -> float:
        """
        Evalúa una expresión en notación RPN.

        Args:
            expr (str): expresión en formato RPN

        Returns:
            float: resultado de la evaluación
        """

        tokens = expr.split()

        for token in tokens:
            try:
                # =====================
                # Operaciones básicas
                # =====================
                if token in ["+", "-", "*", "/"]:
                    b = self.pop()
                    a = self.pop()

                    if token == "+":
                        self.push(a + b)
                    elif token == "-":
                        self.push(a - b)
                    elif token == "*":
                        self.push(a * b)
                    elif token == "/":
                        if b == 0:
                            raise RPNError("División por cero")
                        self.push(a / b)

                # =====================
                # Operaciones de pila
                # =====================
                elif token == "dup":
                    if not self.stack:
                        raise RPNError("Pila insuficiente")
                    self.push(self.stack[-1])

                elif token == "swap":
                    a = self.pop()
                    b = self.pop()
                    self.push(a)
                    self.push(b)

                elif token == "drop":
                    self.pop()

                elif token == "clear":
                    self.stack.clear()

                # =====================
                # Constantes
                # =====================
                elif token == "pi":
                    self.push(math.pi)
                elif token == "e":
                    self.push(math.e)
                elif token == "phi":
                    self.push((1 + math.sqrt(5)) / 2)

                # =====================
                # Funciones matemáticas
                # =====================
                elif token == "sqrt":
                    value = self.pop()
                    if value < 0:
                        raise RPNError("Raíz de número negativo")
                    self.push(math.sqrt(value))

                elif token == "log":
                    value = self.pop()
                    if value <= 0:
                        raise RPNError("Logaritmo indefinido")
                    self.push(math.log10(value))

                elif token == "ln":
                    value = self.pop()
                    if value <= 0:
                        raise RPNError("Logaritmo indefinido")
                    self.push(math.log(value))

                # =====================
                # Trigonometría
                # =====================
                elif token == "sin":
                    self.push(math.sin(math.radians(self.pop())))
                elif token == "cos":
                    self.push(math.cos(math.radians(self.pop())))
                elif token == "tg":
                    self.push(math.tan(math.radians(self.pop())))

                # =====================
                # Trigonometría inversa
                # =====================
                elif token == "asin":
                    self.push(math.degrees(math.asin(self.pop())))
                elif token == "acos":
                    self.push(math.degrees(math.acos(self.pop())))
                elif token == "atan":
                    self.push(math.degrees(math.atan(self.pop())))

                # =====================
                # Operaciones avanzadas
                # =====================
                elif token == "10x":
                    self.push(10 ** self.pop())

                elif token == "y^x":
                    b = self.pop()
                    a = self.pop()
                    self.push(a ** b)

                elif token == "1/x":
                    value = self.pop()
                    if value == 0:
                        raise RPNError("División por cero")
                    self.push(1 / value)

                elif token == "chs":
                    self.push(-self.pop())

                # =====================
                # Memoria
                # =====================
                elif token.startswith("sto"):
                    key = token[3:]
                    if key not in self.mem:
                        raise RPNError("Memoria inválida")
                    self.mem[key] = self.pop()

                elif token.startswith("rcl"):
                    key = token[3:]
                    if key not in self.mem:
                        raise RPNError("Memoria inválida")
                    self.push(self.mem[key])

                # =====================
                # Número
                # =====================
                else:
                    self.push(float(token))

            except ValueError as exc:
                raise RPNError(f"Token inválido: {token}") from exc
            except Exception as exc:
                raise RPNError(str(exc)) from exc

        if len(self.stack) != 1:
            raise RPNError("La pila no terminó con un único valor")

        return self.stack[0]

def run(expr: str) -> float:
    """Función auxiliar para ejecutar una expresión RPN."""
    return RPN().eval(expr)

def main() -> None:
    """Punto de entrada del programa."""
    try:
        expression = input("Ingrese expresión RPN: ")
        rpn = RPN()
        result = rpn.eval(expression)
        print("Resultado:", result)
    except RPNError as exc:
        print("Error:", exc)


if __name__ == "__main__":
    main()