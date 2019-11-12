import os
for subdir, dirs, files in os.walk("./imagenet_data/tf_records/train/"):
    existing_files = files

print(len(existing_files))
for file in existing_files:
    print(file)