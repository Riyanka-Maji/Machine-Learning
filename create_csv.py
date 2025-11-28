import csv

data = [
    ["Roll", "Name", "Marks"],
    [1, "Riya", 85],
    [2, "Aman", 90],
    [3, "Soham", 75],
    [4, "Pri", 76],
    [5, "Shreya",80]
]

with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV Created: student.csv")

with open("student.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("\nHeader:", header)

    print("\nData:")
    for row in reader:
        print(row)
