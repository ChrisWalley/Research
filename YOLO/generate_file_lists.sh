rm data/train.txt
rm data/test.txt
rm data/valid.txt

find data/img -type f -name '*.jpg' >> data/train.txt
find data/img -type f -name '*.jpeg' >> data/train.txt
find data/test_images -type f -name '*.jpg' >> data/test.txt
find data/test_images -type f -name '*.jpeg' >> data/test.txt
find data/validation_images -type f -name '*.jpg' >> data/valid.txt
find data/validation_images -type f -name '*.jpeg' >> data/valid.txt
