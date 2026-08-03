def apply_discount(price, discount):
    if not isinstance(price, (float, int)) or isinstance(price, bool):
        return "The price should be a number"

    if not isinstance(discount, (float, int)) or isinstance(discount, bool):
        return "The discount should be a number"

    if price <= 0:
        return "The price should be greater than 0"
    
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    discount_amount = price * (discount / 100)
    final_price = price - discount_amount
    return final_price

price = input("Enter the price of the product: ")
discount = input("Enter the discount percentage: ")

print(apply_discount(float(price), float(discount)))