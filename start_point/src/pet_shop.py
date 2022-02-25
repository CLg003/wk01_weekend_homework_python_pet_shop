# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, transaction):
    pet_shop["admin"]["total_cash"] += transaction
    return get_total_cash(pet_shop)

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, new_pets_sold):
    pet_shop["admin"]["pets_sold"] += new_pets_sold
    return get_pets_sold(pet_shop)

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pets_by_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets_by_breed.append(pet)
    return pets_by_breed

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
    return None

# def remove_pet_by_name(pet_shop, name):
#     for pet in pet_shop["pets"]:
#         if pet["name"] == name:
#             pet_shop["pets"].remove(pet)

def remove_pet_by_name(pet_shop, name):
    pet_shop["pets"].remove(find_pet_by_name(pet_shop, name))

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    return False

customers = [
            {
                "name": "Alice",
                "pets": [],
                "cash": 1000
            },
            {
                "name": "Bob",
                "pets": [],
                "cash": 50
            },
            {
                "name": "Jack",
                "pets": [],
                "cash": 100
            }
        ]

new_pet = {
    "name": "Bors the Younger",
    "pet_type": "cat",
    "breed": "Cornish Rex",
    "price": 100
}

cc_pet_shop = {
    "pets": [
        {
            "name": "Sir Percy",
            "pet_type": "cat",
            "breed": "British Shorthair",
            "price": 500
        },
        {
            "name": "King Bagdemagus",
            "pet_type": "cat",
            "breed": "British Shorthair",
            "price": 500
        },
        {
            "name": "Sir Lancelot",
            "pet_type": "dog",
            "breed": "Pomsky",
            "price": 1000,
        },
        {
            "name": "Arthur",
            "pet_type": "dog",
            "breed": "Husky",
            "price": 900,
        },
        {
            "name": "Tristan",
            "pet_type": "cat",
            "breed": "Basset Hound",
            "price": 800,
        },
        {
            "name": "Merlin",
            "pet_type": "cat",
            "breed": "Egyptian Mau",
            "price": 1500,
        }
    ],
    "admin": {
        "total_cash": 1000,
        "pets_sold": 0,
    },
    "name": "Camelot of Pets"
}

# def find_pet_by_name(pet_shop, name):
#     for pet in pet_shop["pets"]:
#         if pet["name"] == name:
#             return pet
#     return None

def sell_pet_to_customer(pet_shop, pet, customer):
    if (find_pet_by_name(pet_shop, pet["name"])) == None:
        pass
    if (customer_can_afford_pet(customer, pet) == True):
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"]) # +/-price??
        add_pet_to_customer(customer, pet)
        remove_pet_by_name(pet_shop, pet["name"])
        increase_pets_sold(pet_shop, 1)
    
sell_pet_to_customer(cc_pet_shop, cc_pet_shop["pets"][3], customers[0])
print(get_customer_pet_count(customers[0]))
print(get_pets_sold(cc_pet_shop))
print(get_customer_cash(customers[0]))
print(get_total_cash(cc_pet_shop))


# These are 'integration' tests so we want multiple asserts.
# If one fails the entire test should fail
#
# @unittest.skip("delete this line to run the test")
def test_sell_pet_to_customer__pet_found(self):
    customer = self.customers[0]
    pet = find_pet_by_name(self.cc_pet_shop,"Arthur")

    sell_pet_to_customer(self.cc_pet_shop, pet, customer)

    self.assertEqual(1, get_customer_pet_count(customer))
    self.assertEqual(1, get_pets_sold(self.cc_pet_shop))
    self.assertEqual(100, get_customer_cash(customer))
    self.assertEqual(1900, get_total_cash(self.cc_pet_shop))
    
# @unittest.skip("delete this line to run the test")
def test_sell_pet_to_customer__pet_not_found(self):
    customer = self.customers[0]
    pet = find_pet_by_name(self.cc_pet_shop,"Dave")

    sell_pet_to_customer(self.cc_pet_shop, pet, customer)

    self.assertEqual(0, get_customer_pet_count(customer))
    self.assertEqual(0, get_pets_sold(self.cc_pet_shop))
    self.assertEqual(1000, get_customer_cash(customer))
    self.assertEqual(1000, get_total_cash(self.cc_pet_shop))

# @unittest.skip("delete this line to run the test")
def test_sell_pet_to_customer__insufficient_funds(self):
    customer = self.customers[1]
    pet = find_pet_by_name(self.cc_pet_shop,"Arthur")

    sell_pet_to_customer(self.cc_pet_shop, pet, customer)

    self.assertEqual(0, get_customer_pet_count(customer))
    self.assertEqual(0, get_pets_sold(self.cc_pet_shop))
    self.assertEqual(50, get_customer_cash(customer))
    self.assertEqual(1000, get_total_cash(self.cc_pet_shop))