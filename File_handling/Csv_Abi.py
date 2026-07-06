import csv

data = [
    ["Name", "Age", "City"],
    ["Abi", "20", "Tvm"],
    ["Achu", "21", "Kollam"],
    ["Abijith", "22", "Kochi"],
]

with open("Csv_abi_output.csv", "w", newline="") as f:
    write = csv.writer(f)
    write.writerows(data)

print("Created the csv file !")

with open("Csv_abi_output.csv", "r") as f:
    read = csv.reader(f)
    for row in read:
        print(row)