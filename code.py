products = [
    {"id": 1, "name": "Rice",  "price": 180, "stock": 50},
    {"id": 2, "name": "Tea",   "price": 450, "stock": 8},
    {"id": 3, "name": "Milk",  "price": 90,  "stock": 0},
    {"id": 4, "name": "Sugar", "price": 70,  "stock": 30},
]


for p in products:
    print(f"{p['id']}. {p['name']:^10} Rs {p['price']:^10} stock: {p['stock']}")

def get_low_stock (items , limit=10):
    result= []
    for p in items:
        if p['stock'] < limit:
            result.append(p['name'])
    return result

print(get_low_stock(products))

def find_product(items, name):
    for p in items:
        if p['name'].lower() == name.lower():
            return p

print(find_product(products, "tea"))

def inventory_value(items):
    value = 0
    for p in items:
        value += p['price'] * p['stock']
    return value

print(inventory_value(products))

def sell(items , name , qty):
    p = find_product(items , name)
    if p is None:
        return "Product not found"
    if p['stock'] < qty:
        return f"{p['name']} Only {p['stock']} left"
    p['stock'] -= qty
    return f"Sold {qty} {p['name']}. left {p['stock']}"

print(sell(products, "rice", 5))
print(sell(products, "milk", 1))
print(sell(products, "salt", 1))


products.append({"id": 5, "name": "Bread" , "price": 60, "stock": 20})
products = [p for p in products if p['id'] != 3]
print(len(products))

for p in products:
    print(f"{p['id']}. {p['name']:^10} Rs {p['price']:^10} stock: {p['stock']}")

def get_names(items):
    products_name = []
    for p in items:
        products_name.append(p["name"])
    return products_name

print(get_names(products))


def get_expensive(items , min_price):
    above_min_price = []
    for p in items:
        if p['price'] > min_price:
            above_min_price.append(p)
    return above_min_price        

print(get_expensive(products , 70))

def out_of_stocks(items):
    for p in items:
        if p["stock"] == 0 :
            return p["name"]
print(out_of_stocks(products))

out_of_stock = [p['name'] for p in products if p['stock'] == 0]
print(out_of_stock)


def total_items(items):
    sum = 0
    for p in items:
        sum += p["stock"]
    return sum 
print(total_items(products))   

def restock(items , name , qty):
    p = find_product(items , name)
    if p is None:
        return "product not found"
    p["stock"] += qty
    return items

products = restock(products , "tea" , 20)
print(products)


def most_expensive_item(items):
    value = 0
    for p in items:
        if p["price"] > value:
            value = p["price"]
    return value

print(most_expensive_item(products))

def apply_discount(items , percent):
    per = percent/100
    for p in items:
        p['price'] -= p['price'] * per
    return items    

print(apply_discount(products , 12))

def add_product(items , name , price , stock):
    return items.append({"id": len(items)+1, "name": name, "price": price , "stock": stock})

products = add_product(products , "bat", 1200 , 35)
print(products)