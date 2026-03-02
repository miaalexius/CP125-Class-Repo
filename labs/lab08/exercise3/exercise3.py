# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:

def calculate_order_total(products_file, order_file, output_file):
    '''products = {}

    with open(products_file, "r") as f:
        for line in f:
            name, price = line.strip().split(",")
            products[name] = float(price)
    
    total = 0.0
    
    with open(order_file, "r") as f:
        for line in f:
            product_name, quantity = line.strip().split(",")
            quantity = int(quantity)
            
            if product_name in products:
                total += products[product_name] * quantity
    
    with open(output_file, "w") as f:
        f.write(f"Grand Total: ${total:.2f}\n")
    
    return total'''

    


result = calculate_order_total("labs/lab08/exercise3/data/products.csv", "labs/lab08/exercise3/data/order.csv", "labs/lab08/exercise3/data/total.csv")
