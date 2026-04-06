#AZZA DAMIA BINTI KHAIRUL ZAMAN
#MC2515202749
#C02
#Topic 3: File Handling (CSV)

import csv 

# read BMI data and calculate average height
def read_bmi(filename): 
    data = open( filename , "r", newline ="")
    reader = csv.reader (data)

    print(next(reader))
    total = 0
    count = 0

    for row in reader : 
        print(row)
        total = total + float(row[1])
        count = count + 1

    average = total / count 
    data.close()
    return average

# add new data to the CSV file and display updated content
def add_data(filename): 
    Gender = input("Enter Gender : " )
    Height = input("Enter Height : " )
    Weight = input("Enter Weight : " )
    BMI = input("Enter BMI : " )

    data = open(filename, "a", newline ="")
    writer = csv.writer(data)
    writer.writerow([Gender, Height, Weight, BMI])
    data.close()

    print("\nUpdated File:")

    data = open( filename , "r", newline ="")
    reader = csv.reader (data)

    for row in reader : 
        print(row)
    
    data.close()

# Test the functions
result = read_bmi("bmi.csv")
print ("Average for height : " , result )

add_data("bmi.csv")

