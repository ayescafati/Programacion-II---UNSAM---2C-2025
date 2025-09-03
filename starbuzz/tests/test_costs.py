from beverages import Espresso, DarkRoast, HouseBlend, Beverage
from condiments import Mocha, Whip, Soy

def test_prices_basics():
    # El expresso solo debe costar exactamente 1.99
    assert abs(Espresso().cost() - 1.99) < 1e-9

def test_double_mocha_whip_darkroast():
    # DarkRoast(0.99) + Mocha(0.20) + Whip(0.10) = 1.49
    b = Whip(Mocha(Mocha(DarkRoast())))
    assert abs(b.cost() - 1.49) < 1e-9  # 0.99 + 0.20 + 0.20 + 0.10

def test_size_aware_soy():
    # HouseBlend (0.89) Venti + Soy (0.20) = 1.09
    hb = HouseBlend()
    hb.set_size(Beverage.S_VENTI)
    b = Soy(hb)
    assert abs(b.cost() - (0.89 + 0.20)) < 1e-9

