def file_read(path):
    with open(path) as file:
        data = file.read()
        print(data)

    return file

def write_file(new_path):
    
    with open(new_path, "w") as new_file:
        new_file.write(file)


