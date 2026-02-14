import os

path = "/home/yr/dev"

items = os.listdir(path)

for item in items:
    full_path = os.path.join(path, item)

    if os.path.isdir(full_path):
        print(item, "-> folder")
    else:
        print(item, "-> file")


