import unittest

from shopping_cart import ShoppingCart, UnderflowError


class ShoppingCartTest(unittest.TestCase):

    def setUp(self) -> None:
        self.cart = ShoppingCart()

    def test_empty_cart_contains_0_items(self):
        self.assertEqual(self.cart.item_count(), 0)

    def test_after_adding_item_shopping_cart_contains_1_item(self):
        self.cart.add("Bananas")
        self.assertEqual(self.cart.item_count(), 1)

    def test_after_removing_the_item_shopping_cart_is_empty(self):
        self.cart.add("Bananas")
        self.cart.remove("Bananas")
        self.assertEqual(self.cart.item_count(), 0)

    def test_when_trying_to_remove_item_from_empty_cart_throw_error(self):
        with self.assertRaises(UnderflowError):
            self.cart.remove("Bananas")


class ShoppingCartWithTwoItemsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.cart = ShoppingCart()
        self.cart.add("Bananas")
        self.cart.add("Apples")

    def test_cart_contains_2_items(self):
        self.assertEqual(self.cart.item_count(), 2)
    def test_removing_last_item_results_in_only_first_item(self):
        self.cart.remove("Apples")
        self.assertEqual(self.cart.items(), ["Bananas"])

    def test_removing_first_item_results_in_only_last_item(self):
        self.cart.remove("Bananas")
        self.assertEqual(self.cart.items(), ["Apples"])
