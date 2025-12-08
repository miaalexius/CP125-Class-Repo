# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):
    
    real_budget = ((one_way_km * 2)/km_per_liter) * price_per_liter
    
    if budget >= real_budget:
        return "Enough"
    else :
        return "Not enough"

# Test your code here
print("Testing Road Trip Budgeter...")
