import pandas as pd


def compare_averages(filename):

    df = pd.read_csv(filename)
    print(df.head())
    math_average = float(round(df["Math"].mean(), 1))
    sci_average = float(round(df["Science"].mean(), 1))
    eng_average = float(round(df["English"].mean(), 1))

    averages = {"Math": math_average, "Science": sci_average, "English": eng_average}
    highest = max(averages, key=averages.get)
    lowest = min(averages, key=averages.get)

    averages["best_subject"] = highest
    averages["worst_subject"] = lowest

    return averages

result = compare_averages("labs/lab09/data/students.csv")
print(result)
