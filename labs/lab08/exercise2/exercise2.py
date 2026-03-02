# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):


    f = open(file1, "r")
    f2 = open(file2, "r")
    f3 = open(output_file, "w")

    line1 = f.readlines()
    line2 = f2.readlines()

    merge = set(line1 + line2)
   
    sorted_merge = sorted(merge)
   
    f3.writelines(sorted_merge)

    return len(sorted_merge)

 
# Test your code here
result = merge_lists("labs/lab08/exercise2/data/list1.txt", "labs/lab08/exercise2/data/list2.txt", "labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")
