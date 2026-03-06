import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Name": ["Akshmith", "Roopesh", "Pranvi", "Karan", "Suraksha"],
    "Machine Learning": [85, 78, 92, 74, 88],
    "Python": [90, 82, 89, 76, 91],
    "Java": [80, 76, 95, 72, 84],
    "DBMS": [75, 90, 69, 70, 85]
}
df = pd.DataFrame(data)
print("Student Dataset:\n")
print(df)
print("\nBasic Statistics:\n")
print(df.describe())

df["Average"] = df[["Machine Learning","Python","Java","DBMS"]].mean(axis=1)
print("\nDataset with Average Marks:\n")
print(df)

plt.figure()
plt.bar(df["Name"], df["Python"], color="skyblue")
plt.title("Python Marks of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

plt.figure()
plt.plot(df["Name"], df["Machine Learning"], marker='o', color="green")
plt.title("Machine Learning Marks of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()