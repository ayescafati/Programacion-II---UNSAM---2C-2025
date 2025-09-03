# beverages.py
# Contiene el Componente y los Componentes Concretos del patrón.

from abc import ABC, abstractmethod

# --- Componente Abstracto ---
class Beverage(ABC):
    """
    La clase base para todas las bebidas. Utiliza el módulo abc para
    definir que es una clase abstracta.
    """
    S_TALL = "Tall"
    S_GRANDE = "Grande"
    S_VENTI = "Venti"
    
    VALID_SIZES = {S_TALL, S_GRANDE, S_VENTI}

    def __init__(self):
        self.description = "Bebida Desconocida"
        self._size = Beverage.S_TALL # por default

    def set_size(self, size: str):
        if size not in Beverage.VALID_SIZES:
            raise ValueError(
                f"Tamaño inválido: '{size}'."
                f"Debe ser uno de {Beverage.VALID_SIZES}"
            )
        self._size = size

    def get_size (self) -> str:
        return self._size

    def get_description(self) -> str:
        """
        Devuelve la descripción de la bebida.
        """
        return self.description

    @abstractmethod
    def cost(self) -> float:
        """
        Método abstracto que las subclases deben implementar para devolver
        el costo de la bebida.
        """
        pass

# --- Componentes Concretos ---
class HouseBlend(Beverage):
    """
    Café de la casa, un tipo específico de bebida.
    """
    def __init__(self):
        super().__init__()
        self.description = "Café de la Casa"

    def cost(self) -> float:
        return 0.89

class DarkRoast(Beverage):
    """
    Café Dark Roast, un tipo específico de bebida.
    """
    def __init__(self):
        super().__init__()
        self.description = "Café Dark Roast"

    def cost(self) -> float:
        return 0.99

class Decaf(Beverage):
    """
    Café Descafeinado, un tipo específico de bebida.
    """
    def __init__(self):
        self.description = "Café Descafeinado"

    def cost(self) -> float:
        return 1.05

class Espresso(Beverage):
    """
    Café Espresso, un tipo específico de bebida.
    """
    def __init__(self):
        super().__init__()
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99
