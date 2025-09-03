from starbuzz.beverages import Espresso, DarkRoast, HouseBlend, Beverage
from starbuzz.condiments import Mocha, Whip, Soy

def test_prices_basics():
    assert abs(Espresso().cost() - 1.99) < 1e-9

def test_double_mocha_whip_darkroast():
    b = Whip(Mocha(Mocha(DarkRoast())))
    assert abs(b.cost() - 1.49) < 1e-9  # 0.99 + 0.20 + 0.20 + 0.10

def test_size_aware_soy():
    hb = HouseBlend()
    hb.set_size(Beverage.S_VENTI)
    b = Soy(hb)
    assert abs(b.cost() - (0.89 + 0.20)) < 1e-9
