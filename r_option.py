with open("file.txt", "r") as file:
    line =file.readline()
    while line:
        print(line.rsplit())
        line = file.readline()
