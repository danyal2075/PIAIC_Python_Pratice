path = "writefile.txt"

with open(path, "a") as file:   # "a" is used to append the file. otherwise w is used
    file.write("Hello World")