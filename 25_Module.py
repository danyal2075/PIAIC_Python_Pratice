import file_operation

path = "./datafile.txt"
new_path = "./new_datafile.txt"

data = file_operation.file_read(path)

file_operation.write_file(new_path)
    