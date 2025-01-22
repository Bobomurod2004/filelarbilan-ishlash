try:
    with open("file.txt", "x") as file:
        file.write("Fayl yangi")
except FileExistsError:
    print("fayl yaratilgan")