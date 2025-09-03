# main.py
# Script principal para probar el patrón Decorator.

from beverages import Espresso, DarkRoast, HouseBlend, Beverage
from condiments import Mocha, Whip, Soy, Caramel  # <- importa Caramel
from builder import build_beverage   # importa builder


def main():
    """
    Función principal que simula la preparación de cafés en Starbuzz.
    """
    print("Bienvenido a Starbuzz Coffee!")
    print("--- Preparando pedidos ---")

    # Pedido 1: Un Espresso simple, sin condimentos.
    beverage1 = Espresso()
    print(f"Pedido 1: {beverage1.get_description()} ${beverage1.cost():.2f}")

    # Pedido 2: Un DarkRoast con doble Mocha y Crema.
    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)  # Envolvemos con el primer Mocha
    beverage2 = Mocha(beverage2)  # Envolvemos con el segundo Mocha
    beverage2 = Whip(beverage2)   # Envolvemos con Crema
    print(f"Pedido 2: {beverage2.get_description()} ${beverage2.cost():.2f}")

    # Pedido 3: Un HouseBlend con Soja, Mocha y Crema.
    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"Pedido 3: {beverage3.get_description()} ${beverage3.cost():.2f}")

    # Pedido 4: Espresso con Caramelo y Crema
    beverage4 = Caramel(Espresso())
    beverage4 = Whip(beverage4)
    print(f"Pedido 4: {beverage4.get_description()} ${beverage4.cost():.2f}")

    # Ejemplo 1: HouseBlend Venti + Soy
    hb = HouseBlend()
    hb.set_size(Beverage.S_VENTI)
    hb = Soy(hb)
    print(f"Ej 1: {hb.get_description()} ({hb.get_size()}) ${hb.cost():.2f}")

    # Ejemplo 2: DarkRoast Grande + doble Mocha + Crema
    dr = DarkRoast();dr.set_size(Beverage.S_GRANDE)
    dr = Mocha(Mocha(Whip(dr)))
    print(f"EJ 2: {dr.get_description()}({dr.get_size()}) ${dr.cost():.2f}")

    # Pedido con builder
    order = build_beverage(HouseBlend(), Beverage.S_VENTI, ["soy", "mocha", "whip"])
    print(f"Pedido 5 (builder): {order.get_description()} ({order.get_size()}) ${order.cost():.2f}")
    

if __name__ == "__main__":
    main()