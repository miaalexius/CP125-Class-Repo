import pandas as pd

def explore_data(filename):
    df = pd.read_csv(filename)

    total_students = len(df)
    list_of_subjects = ["Math", "Science", "English"]
    math_average = float(round(df["Math"].mean(), 1))
    highest_math_student = df.loc[df["Math"].idxmax(), "Name"]

    return {
        "total_students": total_students,
        "subjects": list_of_subjects,
        "math_average": math_average,
        "highest_math_student": highest_math_student
    }

# Test the function
results = explore_data("labs/lab09/data/students.csv")
for key, value in results.items():
    print(f"{key}: {value}")