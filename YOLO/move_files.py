import os
import shutil

train_path = 'ISL_data/img'
test_path = 'ISL_data/test_images'
valid_path = 'ISL_data/validation_images'

# list to store files
res = []
files = os.listdir(train_path)

count = 0
moved = 0
for filename in files:
    # check if current path is a file
    filepath = os.path.join(train_path, filename)

    if os.path.isfile(filepath):

        if '.jpg' in filename:
            text_filename = filename.replace(".jpg", ".txt")
        else:
            continue

        text_filepath = os.path.join(train_path, text_filename)

        if count % 10 == 0:
            if moved % 4 == 0:
                new_filepath = os.path.join(test_path, filename)
                new_text_filepath = os.path.join(test_path, text_filename)
            else:
                new_filepath = os.path.join(valid_path, filename)
                new_text_filepath = os.path.join(valid_path, text_filename)

            shutil.move(filepath, new_filepath)
            shutil.move(text_filepath, new_text_filepath)

            print('Moved', filename, 'and', text_filename, 'to', 'test' if moved % 4 == 0 else 'valid')
            moved += 1
        count += 1

print(moved)