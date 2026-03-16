# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:

def filter_passing_scores(input_file, output_file):
    f = open(input_file, "r")
    f2 = open(output_file, "w")
    
    passing_count = 0
    lines = f.readlines()

    for line in lines:
        parts = line.strip().split()
        
        score = float(parts[1])
            
        if score >= 80:
            f2.write(line)
            passing_count += 1
    
    f.close()
    f2.close()

    return passing_count

result = filter_passing_scores("labs/lab08/exercise1/data/scores.txt", "labs/lab08/exercise1/data/passing.txt")
print(f"Passing students: {result}")
