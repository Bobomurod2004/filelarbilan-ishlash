file=open("file.txt", "r")
contant=file.read()
print(contant)
file.close()

with open("file.txt", "r") as file:
    contant=file.read()
    print(contant)