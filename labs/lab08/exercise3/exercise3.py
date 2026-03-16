# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:

def calculate_order_total(products_file, order_file, output_file):
    f_product = open(products_file, "r")
    f_order = open(order_file, "r")
    f_out = open(output_file, "w")

    f_product.readline() 
    prices = {}
    for line in f_product:
        parts = line.strip().split(",")
        if len(parts) >= 3:
            prod_id = parts[0]
            price = float(parts[2])
            prices[prod_id] = price

    f_order.readline() 
    f_out.write("product_id,total_cost\n") 
    
    grand_total = 0.0
    
    for line in f_order:
        parts = line.strip().split(",")
        if len(parts) == 2:
            prod_id = parts[0]
            quantity = int(parts[1])
            
            if prod_id in prices:
                item_total = prices[prod_id] * quantity
                grand_total += item_total
                
                f_out.write(f"{prod_id},{item_total:.2f}\n")

    f_product.close()
    f_order.close()
    f_out.close()

    return grand_total

result = calculate_order_total("labs/lab08/exercise3/data/products.csv", "labs/lab08/exercise3/data/order.csv", "labs/lab08/exercise3/data/total.csv")
