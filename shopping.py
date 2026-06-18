products = ["Nike Shoes", "Adidas Shoes", "Puma Shoes", "Reebok Shoes"]
prices = [3000, 2500, 2000, 3500]

# Bubble Sort (Ascending Price)
for i in range(len(prices)):
    for j in range(len(prices) - i - 1):
        if prices[j] > prices[j + 1]:
            prices[j], prices[j + 1] = prices[j + 1], prices[j]
            products[j], products[j + 1] = products[j + 1], products[j]

print("Products sorted by price:\n")
for i in range(len(products)):
    print(products[i], "- ₹", prices[i])

item = input("\nEnter product to search: ")

found = False
for i in range(len(products)):
    if products[i].lower() == item.lower():
        print("\nProduct Found!")
        print("Brand:", products[i])
        print("Price: ₹", prices[i])
        found = True
        break

if not found:
    print("Product not found")