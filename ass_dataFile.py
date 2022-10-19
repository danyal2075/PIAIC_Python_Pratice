





path = "./datafile.txt"
x = 0
with open(path) as file:
    data = file.readlines()
    #print(file.readlines())
for line in data:
    #print(line)
    if line == "\n":
        x += 1
        continue
    with open(f"ass{x}.txt",'a ') as new_file:
        new_file.write(line)