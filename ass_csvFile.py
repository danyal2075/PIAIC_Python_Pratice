
path = "./Sample_CSV.csv"

with open(path) as csv_file:
    data = csv_file.readlines()
    #print(data)
for i in data:
    csv = []
    if i == "\n":
        continue 
    csv.append(i)
    print(csv)