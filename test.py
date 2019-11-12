import os
subdir, dirs, existing_files = os.walk("./imagenet_data/tf_records/train/")

print(len(existing_files))
for file in existing_files:
    print(file)