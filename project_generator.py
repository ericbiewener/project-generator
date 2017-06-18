import os
import sys
import fileinput
import shutil

IGNORED_FILES = ['.DS_Store']
IGNORED_FILE_TYPES = ['.pyc']
IGNORED_DIRS = ['.git', 'node_modules']

_, src, name = sys.argv
if not os.path.isdir(src):
    print('Not a directory: {}'.format(src))
    exit()

name_capitalized = name[0].upper() + name[1:]
name_lowercase = name[0].lower() + name[1:]

def replace(text):
    return text.replace('__Base', name_capitalized).replace('__base', name_lowercase)

cwd = os.getcwd()
dest = os.path.join(cwd, name)

for directory, subdirs, files in os.walk(src):
    if directory in IGNORED_DIRS:
        continue

    new_dir = replace(directory)
    os.mkdir(new_dir)

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
