import pandas as pd
import matplotlib.pyplot as plt


def show_math_trend(filename):
    df =pd.read_csv(filename)  
    Math = df["Math"]
    plt.plot(df.index, Math) 
    plt.xlabel("Student Index")
    plt.ylabel("Math Score")
    plt.title("Math Score Trends")
    plt.show()

    return len(df)

result = show_math_trend("labs/lab09/data/students.csv")
print(result)

