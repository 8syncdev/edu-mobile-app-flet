'''
    Author: Nguyễn Phương Anh Tú
    ID: 21110105
'''
'''
The main purpose of this code is to scan a directory named tech for image files (with extensions .png, .jpg, and .jpeg), and then write the filenames of these images into a file named data.txt, appending each filename with a comma.
'''
import os

list_dir = os.listdir("./tech")

#* for each all files in sub folder
for item in list_dir:
    #* check if the file is an image
    if item.endswith(".png") or item.endswith(".jpg") or item.endswith(".jpeg"):
        #* write the import statement to a file
        with open("./data.txt", "a", encoding='utf-8') as f:
            f.write(f'''\'{item}\''''+',')