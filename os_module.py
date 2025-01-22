import os


file_path="file.txt"
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"file{file_path} o'chirildi")
else:
    print("fayl mavjud emas")