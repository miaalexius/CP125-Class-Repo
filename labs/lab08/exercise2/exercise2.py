# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    f = open(file1, "r")
    f2 = open(file2, "r")
    f3 = open(output_file, "w")

    content1 = [line.strip() for line in f.readlines() if line.strip()]
    content2 = [line.strip() for line in f2.readlines() if line.strip()]

    merged_set = set(content1 + content2)
    
    sorted_merge = sorted(merged_set)
    
    for item in sorted_merge:
        f3.write(item + "\n")

    f.close()
    f2.close()
    f3.close()

    return len(sorted_merge)

# Test your code here
result = merge_lists("labs/lab08/exercise2/data/list1.txt", "labs/lab08/exercise2/data/list2.txt", "labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")
