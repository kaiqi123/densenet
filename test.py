import os
for subdir, dirs, files in os.walk("./imagenet_data/tf_records/train/"):
    print(subdir, dirs, files)