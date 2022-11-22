import os
import shutil

train_path = 'data/img'

files = os.listdir(train_path)

not_jpg = []

for filename in files:
    # check if current path is a file
    filepath = os.path.join(train_path, filename)

    if '.jpg' not in filename and 'txt' not in filename:
        not_jpg.append(filename)

for filename in not_jpg:
    if 'jpeg' in filename:
        text_filename = filename.replace('jpeg', 'txt')
        if text_filename not in files:
            print(filename)