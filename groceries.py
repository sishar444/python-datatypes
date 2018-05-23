# groceries.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# Challenge 1
# print(products)

# Challenge 2
# print(products[0])

# Challenge 3
# print(products[0]["name"])

# Challenge 4
# print(len(products))

# Challenge 5
# for product in products:
#     print(product["name"])

# Challenge 6 & 7
def product_name(product):
    return product["name"]

sorted_products = sorted(products, key=product_name)
print("--------------\n" + "THERE ARE " + str(len(sorted_products)) + " PRODUCTS:" + "\n--------------")
for product in sorted_products:
    print(" + " + product["name"] + " (${0:.2f})".format(product["price"]))

# Challenge 8 & 9
# dept_list = []
# for product in products:
#     if product["department"] not in dept_list:
#         dept_list.append(product["department"])
#
# print("--------------\n" + "THERE ARE " + str(len(dept_list)) + " DEPARTMENTS:" + "\n--------------")
# for department in dept_list:
#     print(" + " + department.title())

# # Challenge 10
# dept_list = []
# for product in products:
#     if product["department"] not in dept_list:
#         dept_list.append(product["department"])
#
# print("--------------\n" + "THERE ARE " + str(len(dept_list)) + " DEPARTMENTS:" + "\n--------------")
# sorted_dept_list = sorted(dept_list)
# for department in sorted_dept_list:
#     print(" + " + department.title())

# Challenge 11 & 12
def products_by_dept(department):
    return [product for product in products if product["department"] == department]

dept_list = []
for product in products:
    if product["department"] not in dept_list:
        dept_list.append(product["department"])

print("--------------\n" + "THERE ARE " + str(len(dept_list)) + " DEPARTMENTS:" + "\n--------------")
sorted_dept_list = sorted(dept_list)
for department in sorted_dept_list:
    str_product = "product"
    dept_product_list = products_by_dept(department)
    if len(dept_product_list) > 1:
        str_product = "products"
    print(" + " + department.title() + " (" + str(len(dept_product_list)) + " " + str_product + ")")
