import os
import sys
import fileinput
import shutil

IGNORED_FILES = ['.DS_Store']
IGNORED_FILE_TYPES = ['.pyc']
IGNORED_DIRS = ['.git', 'node_modules']

_, src, old_name, new_name = sys.argv
if not os.path.isdir(src):
    print('Not a directory: {}'.format(src))
    exit()

old_name_capitalized = old_name[0].upper() + old_name[1:]
old_name_lowercase = old_name[0].lower() + old_name[1:]
new_name_capitalized = new_name[0].upper() + new_name[1:]
new_name_lowercase = new_name[0].lower() + new_name[1:]

def replace(text):
    return text.replace(old_name_capitalized, new_name_capitalized).replace(old_name_lowercase, new_name_lowercase)

cwd = os.getcwd()

for directory, subdirs, files in os.walk(src, topdown=False):
    if directory in IGNORED_DIRS:
        continue

    new_dir = replace(directory)
    if not os.path.isdir(new_dir):
        if os.path.isdir(os.path.dirname(new_dir)):
            os.mkdir(new_dir)
        else:
            # Build entire directory tree if necessary
            os.makedirs(new_dir)

    for file in files:
        if file in IGNORED_FILES:
            continue

        _, ext = os.path.splitext(file)
        if ext in IGNORED_FILE_TYPES:
            continue

        src_file = os.path.join(directory, file)
        with open(src_file, 'rb') as f:
            text = f.read()

        new_file = os.path.join(new_dir, replace(file))
        with open(new_file, 'w') as f:
            f.write(replace(text))

        os.remove(src_file)

    if new_dir != directory:
        shutil.rmtree(directory)
