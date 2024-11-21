class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        return f"Titular: {self.titular}, Cantidad: {self.cantidad:.2f}"

    def ingresar(self, monto):
        if monto > 0:
            self.cantidad += monto

    def retirar(self, monto):
        if monto > 0:
            self.cantidad -= monto


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    # Setters y Getters para la bonificación
    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def get_bonificacion(self):
        return self.bonificacion

    # Verifica si el titular es válido
    def esTitularValido(self, edad):
        return 18 <= edad < 25

    # Sobrescribe el método retirar
    def retirar(self, monto, edad):
        if self.esTitularValido(edad):
            super().retirar(monto)
        else:
            print("Retiro no permitido: titular no válido.")

    # Muestra información de la cuenta joven
    def mostrar(self):
        return f"Cuenta Joven - Titular: {self.titular}, Cantidad: {self.cantidad:.2f}, Bonificación: {self.bonificacion:.2f}%"


# Ejemplo de uso
if __name__ == "__main__":
    titular = "daniel torres"
    edad = 22
    cuenta_joven = CuentaJoven(titular, cantidad=1000, bonificacion=10)

    print(cuenta_joven.mostrar())  # Mostrar la información de la cuenta joven

    # Intentar retirar dinero
    cuenta_joven.retirar(100, edad)
    print(cuenta_joven.mostrar())

    # Intentar retirar con un titular no válido
    edad_no_valida = 30
    cuenta_joven.retirar(100, edad_no_valida)
    print(cuenta_joven.mostrar())

