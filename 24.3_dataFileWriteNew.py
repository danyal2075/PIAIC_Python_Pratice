path = "./datafile.txt"
new_path = "./new_datafile.txt"

with open(path) as file:
    data = file.read()
    print(data)
    with open(new_path, "w") as new_file:
        new_file.write(data)