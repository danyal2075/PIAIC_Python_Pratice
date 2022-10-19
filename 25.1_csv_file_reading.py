import csv
path = "./Sample_CSV.csv"

with open(path) as csv_file:
    data = csv.reader(csv_file)
    for i in data:
        print(i) 