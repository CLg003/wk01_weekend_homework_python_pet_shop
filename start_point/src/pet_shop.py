# WRITE YOUR FUNCTIONS HERE

# from ps_class import *

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, transaction):
    pet_shop["admin"]["total_cash"] += transaction
    return get_total_cash(pet_shop)

# ## @unittest.skip("delete this line to run the test")
#     def test_total_cash(self):
#         sum = get_total_cash(self.cc_pet_shop)
#         self.assertEqual(1000, sum)

#     # @unittest.skip("delete this line to run the test")
#     def test_add_or_remove_cash__add(self):
#         add_or_remove_cash(self.cc_pet_shop,10)
#         cash = get_total_cash(self.cc_pet_shop)
#         self.assertEqual(1010, cash)

#     @unittest.skip("delete this line to run the test")
#     def test_add_or_remove_cash__remove(self):
#         add_or_remove_cash(self.cc_pet_shop,-10)
#         cash = get_total_cash(self.cc_pet_shop)
#         self.assertEqual(990, cash)