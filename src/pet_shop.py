def get_pet_shop_name(pet_shop):
    return pet_shop['name']

def get_total_cash(pet_shop):
    return pet_shop['admin']['total_cash']

def add_or_remove_cash(pet_shop, cash):
    pet_shop['admin']['total_cash'] += cash

def get_pets_sold(pet_shop):
    return pet_shop['admin']['pets_sold']

def increase_pets_sold(pet_shop, pet):
    pet_shop['admin']['pets_sold'] += pet

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    amount_of_breed = []
    index = 0
    for pet in "pets":
        if pet_shop["pets"][index]["breed"] == breed:
            amount_of_breed.append(pet)
            index += 1
    return amount_of_breed

def find_pet_by_name(pet_shop, name):
  for pet in pet_shop["pets"] :
        if pet["name"] == name:
            return pet
  
def find_pet_by_name(pet_shop, name):
  for pet in pet_shop["pets"] :
        if pet["name"] == name :
            return pet
           
def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"] :
        if pet["name"] == name :
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, pet) :
    if pet_shop["pets"].append(pet):
        len(pet_shop["pets"])

def get_customer_cash(customers):
    return customers['cash']

def remove_customer_cash(customer, cash):
    customer['cash'] -= cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer['pets'].append(pet)
        

