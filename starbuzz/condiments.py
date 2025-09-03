# condiments.py
# Contiene el Decorador Abstracto y los Decoradores Concretos.

from abc import ABC, abstractmethod
from beverages import Beverage

# --- Decorador Abstracto ---
class CondimentDecorator(Beverage, ABC):
    """
    Clase base para los decoradores de condimentos.
    Hereda de Beverage para tener el mismo tipo.
    Mantiene una referencia a la bebida que está envolviendo.
    """
    def __init__(self, beverage: Beverage):
        super().__init__()  # asegura interfaz Beverage
        self._beverage = beverage
    
    # Propagación del tamaño: el tamaño es el del beverage 
    def set_size (self, size: str):
        self._beverage.set_size(size)

    def get_size(self) -> str:
        return self._beverage.get_size()
    

    @abstractmethod
    def get_description(self) -> str:
        pass


# --- Decoradores Concretos ---
class Milk(CondimentDecorator):
    """
    Decorador para añadir Leche a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Leche"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10

class Mocha(CondimentDecorator):
    """
    Decorador para añadir Mocha a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Mocha"

    def cost(self) -> float:
        return self._beverage.cost() + 0.20

class Soy(CondimentDecorator):
    """
    Decorador para añadir Soja a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Soja"

    def cost(self) -> float:
        base = self._beverage.cost()
        size = self.get_size()
        extra = 0.10
        if size == Beverage.S_GRANDE:
            extra = 0.15
        elif size == Beverage.S_VENTI:
            extra = 0.20
        return base + extra
        #return self._beverage.cost() + 0.15
        


class Whip(CondimentDecorator):
    """
    Decorador para añadir Crema a una bebida.
    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Crema"

    def cost(self) -> float:
        return self._beverage.cost() + 0.10

class Caramel(CondimentDecorator):
    """
    Decorador para añadir Caramelo a una bebida.
    
    Consigna:
    Implementar `Caramel` (Caramelo) con un costo fijo (p. ej., `$0.20`).  
    Actualizar `get_description()` y `cost()` como en `Mocha`.  

    """
    def get_description(self) -> str:
        return self._beverage.get_description() + ", Caramelo"

    def cost(self) -> float:
        return self._beverage.cost() + 0.20
