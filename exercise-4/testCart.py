from cart import Cart
import pytest

# Cart instance
new_cart = Cart()

def test_add_item():
    new_cart.add_item("Tooth Paste")
    item = new_cart.items.index("Tooth Paste")
    assert new_cart.items[item] == "Tooth Paste"


def test_remove_item():
    new_cart.remove_item("Tooth Paste")
    item = new_cart.items.index("Tooth Paste") if "Tooth Paste" in new_cart.items else -1
    assert item == -1


def test_items_total():
    new_cart.add_item("Tooth Paste")
    total = new_cart.calculating_totals()
    assert total == 1

def test_add_item_type():
    new_cart.add_item(2)
    total = new_cart.calculating_totals()
    assert total != 2
    
def test_remove_item_type():
    new_cart.remove_item(2)
    total = new_cart.calculating_totals()
    assert total != 0