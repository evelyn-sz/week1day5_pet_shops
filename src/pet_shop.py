# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop_name):
    return pet_shop_name["name"]

def get_total_cash(total_cash):
    return total_cash["admin"]["total_cash"]

def add_or_remove_cash(total_cash, number):
    total_cash["admin"]["total_cash"] += number

def add_or_remove_cash__remove(total_cash, number):
    total_cash["admin"]["total_cash"] += number

def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]

# 6
def increase_pets_sold(pets_sold, number):
    pets_sold["admin"]["pets_sold"] += number

# 7
def get_stock_count(stock_count):
    return len(stock_count["pets"])
    
# 8
def get_pets_by_breed(pets, breed):
    pet_breeds = []
    for pet in pets:
        if pet["breed"] == breed:
            pet_breeds.append(pet["breed"])
    return pet_breeds