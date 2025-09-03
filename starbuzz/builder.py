from typing import Iterable
from beverages import Beverage
from condiments import Milk, Mocha, Soy, Whip, Caramel

CONDIMENTS_MAP = {
    "milk": Milk,
    "mocha": Mocha,
    "soy": Soy,
    "whip": Whip,
    "caramel": Caramel,
}

def build_beverage(base: Beverage, size: str, condiments: Iterable[str]) -> Beverage:
    base.set_size(size)
    b = base
    for name in condiments:
        cls = CONDIMENTS_MAP[name.lower()]
        b = cls(b)
    return b
