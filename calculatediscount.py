def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price


# Example 1: Applying a 20% discount on a $100 item
example_price_1 = 100
example_discount_1 = 25
print(f"Example 1 - Original price: ${example_price_1}, Discount: {example_discount_1}%")
print(f"Final price: ${calculate_discount(example_price_1, example_discount_1)}\n")

# Example 2: Applying a 20% discount on a $50 item
example_price_2 = 50
example_discount_2 = 10
print(f"Example 2 - Original price: ${example_price_2}, Discount: {example_discount_2}%")
print(f"Final price: ${calculate_discount(example_price_2, example_discount_2)}\n")

# Example 3: Applying a 0% discount on a $200 item
example_price_3 = 200
example_discount_3 = 30
print(f"Example 3 - Original price: ${example_price_3}, Discount: {example_discount_3}%")
print(f"Final price: ${calculate_discount(example_price_3, example_discount_3)}\n")

# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percent)

# Print the final price
print(f"The final price after applying the discount is: {final_price}")
