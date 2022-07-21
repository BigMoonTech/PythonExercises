import random

food = random.choice(["morning bun", "toffee cookie"])

bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

for item,quantity in bakery_stock.items():
    if food == item:
        print(str(quantity) + " left")
    else:
        print("We don't make that")
