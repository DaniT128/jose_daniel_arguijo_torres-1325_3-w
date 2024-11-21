class Persona:
    def __init__(self, nombre="" , edad=0, dni=""):
        # Constructor con valores predeterminados vacíos o 0 para edad
        self.set_nombre(nombre)
        self.set_edad(edad)
        self.set_dni(dni)
    
    # Setters y Getters para nombre
    def set_nombre(self, nombre):
        if isinstance(nombre, str) and len(nombre) > 0:
            self.nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía.")
    
    def get_nombre(self):
        return self.nombre
    
    # Setters y Getters para edad
    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self.edad = edad
        else:
            raise ValueError("La edad debe ser un número entero positivo.")
    
    def get_edad(self):
        return self.edad
    
    # Setters y Getters para DNI
    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 9 and dni[-1].isalpha() and dni[:-1].isdigit():
            self.dni = dni
        else:
            raise ValueError("El DNI debe tener 9 caracteres: 8 dígitos seguidos de una letra.")
    
    def get_dni(self):
        return self.dni
    
    # Método para mostrar los datos de la persona
    def mostrar(self):
        print(f"Nombre: {self.get_nombre()}")
        print(f"Edad: {self.get_edad()}")
        print(f"DNI: {self.get_dni()}")
    
    # Método para determinar si es mayor de edad
    def es_mayor_de_edad(self):
        return self.get_edad() >= 18


# Ejemplo de uso
try:
    persona = Persona(nombre="daniel", edad=19, dni="12345678Z")
    persona.mostrar()
    print(f"¿Es mayor de edad? {'Sí' if persona.es_mayor_de_edad() else 'No'}")
except ValueError as e:
    print(f"Error: {e}")

