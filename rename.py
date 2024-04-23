import os

join = os.path.join

for root, dirs, files in os.walk("config"):
    for f in files:
        if ":" in f:
            print("renaming from ", join(root, f), " to ", join(root, f.replace(":", "_")))
            # os.rename(join(root, f), join(root, f.replace(":", "_")))
        if "?" in f:
            print("renaming from ", join(root, f), " to ", join(root, f.replace("?", "_")))
            # os.rename(join(root, f), join(root, f.replace("?", "_")))
    # print(root, dirs, files)
