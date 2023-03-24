@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False


class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.__id = Conjunto.contador
        Conjunto.contador += 1
        self.nombre = nombre
        self.__elementos = []

    def id(self):
        return self.__id

    def contiene(self, elemento):
        return any(e == elemento for e in self.__elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.__elementos.append(elemento)

    def unir(self, otro):
        for e in otro.__elementos:
            self.agregar_elemento(e)

    def __add__(self, otro):
        resultado = Conjunto(f"{self.nombre} + {otro.nombre}")
        resultado.unir(self)
        resultado.unir(otro)
        return resultado

    def intersectar(cls, conjunto1, conjunto2):
        nombre = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        resultado = Conjunto(nombre)
        for e in conjunto1.__elementos:
            if conjunto2.contiene(e):
                resultado.agregar_elemento(e)
        return resultado

    def __str__(self):
        elementos = ", ".join(str(e.nombre) for e in self.__elementos)
        return f"Conjunto {self.nombre}: ({elementos})"