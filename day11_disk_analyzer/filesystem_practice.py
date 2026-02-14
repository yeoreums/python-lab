import os

def count_folders(path):
    total = 0
    
    for root, dirs, files in os.walk(path):

        total += len(dirs)
        
    return total
    

path = "/home/yr/dev"
print("Total folders:", count_folders(path))
