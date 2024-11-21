class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        
        if titular is None:
            raise ValueError("El titular de la cuenta es obligatorio.")
        self.titular = titular
        self.set_cantidad(cantidad)  
    
    
    def set_titular(self, titular):
        if titular is None:
            raise ValueError("El titular no puede ser None.")
        self.titular = titular
    
    def get_titular(self):
        return self.titular

    
    def set_cantidad(self, cantidad):
        if not isinstance(cantidad, (int, float)) or cantidad < 0:
            raise ValueError("La cantidad debe ser un número mayor o igual a cero.")
        self.cantidad = cantidad
    
    def get_cantidad(self):
        return self.cantidad

    
    def mostrar(self):
        print(f"Titular: {self.get_titular().get_nombre()}")
        print(f"Cantidad en la cuenta: {self.get_cantidad()}")

    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
        else:
            print("La cantidad a ingresar debe ser positiva.")

    
    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad
        else:
            print("La cantidad a retirar debe ser positiva.")

class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def get_dni(self):
        return self.dni
    
    def es_mayor_de_edad(self):
        return self.edad >= 18

persona = Persona("Juan", 30, "12345678A")

cuenta = Cuenta(titular=persona, cantidad=1000)

cuenta.mostrar()

cuenta.ingresar(500)
cuenta.mostrar()
cuenta.retirar(200)
cuenta.mostrar()
cuenta.retirar(-50)



