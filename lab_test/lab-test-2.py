'''
NAME : AZZA DAMIA BINTI KHAIRUL ZAMAN
Create a program that accepts 5 integer input values from the user and is stored in a
list. The program will perform the following task:
1. Print all the numbers that has been entered in ascending order
2. Calculate and find the sum of all the entered numbers
3. Find and print the largest number  '''

def number_processes () : 
    list_number = []

    #Input numbers for 5 times 
    for i in range (1,6): 
        number = int(input(f"Enter number {i} : "))
        list_number.append(number)
    

    list_number.sort()
    sum_number = sum(list_number)
    largest_number = max(list_number)

    return f"Numbers in ascending order : {list_number} \nSum of all numbers : {sum_number} \nLargest number : {largest_number}"


result = number_processes()
print(result)