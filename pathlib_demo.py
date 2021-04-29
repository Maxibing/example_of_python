#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :usage of pathlib
@Date     :2021/04/29 11:07:44
@Author      :xbMa
'''
import os
import datetime

from pathlib import Path
from prettytable import PrettyTable
from os import chdir
from shutil import copyfile

# Current dir and Home dir
print(f'Current directory: {Path.cwd()}')
print(f'Home directory: {Path.home()}')

# Get current working dir
path = Path()
print(f'Current working directory: {path.cwd()}')

# Change current woriking dir
_cwd = path.cwd()
chdir("..")
print(f'Current working directory: {path.cwd()}')
chdir(_cwd)

# joint path with  /
path_home = Path.home()
docs = path_home / "Documents"
pictures = path_home / "Pictures"
print(docs)
print(pictures)

# Touch a file
Path("newfile.txt").touch()

# Rename file or dir
Path("newfile.txt").rename("rename_newfile.txt")

# Remove file
Path("rename_newfile.txt").unlink()

# Different path format
path = Path('C:/Users/Jano/Downloads/wordpress-5.1.tar.gz')
print(path.as_uri())
print(path.as_posix())

# Relative path
path = Path('C:/Users/DELL/Downloads/wordpress-5.1.tar.gz')
home = Path.home()
relative = path.relative_to(home)
print(relative)

# Parent and Parents
path = Path('C:/Users/DELL/Downloads/wordpress-5.1.tar.gz')
print(f"The parent directory of {path} is {path.parent}")
print(list(path.parents))

# Parts
path= Path().cwd()
print(path.parts)
print(path.drive)
print(path.root)
path = Path('C:/Users/Jano/Downloads/wordpress-5.1.tar.gz')
print(f"The stem is: {path.stem}")
print(f"The name is: {path.name}")
print(f"The suffix is: {path.suffix}")
print(f"The anchor is: {path.anchor}")
print(f"File name: {os.path.splitext(path.stem)[0]}")
print("The suffixes: ")
print(path.suffixes)

# Path.iterdir
path= Path().cwd()
dirs = [i for i in path.iterdir() if i.is_dir()]
files = [i for i in path.iterdir() if i.is_file()]
print(dirs)
print(files)

# Create a new dir
path = Path.cwd() / 'new'
path.mkdir()

# Remove dir
path.rmdir()

# Copy file
source = Path("smtplib_test_file.txt")
destination = Path("smtplib_test_file_new.txt")
copyfile(source, destination)
Path("smtplib_test_file_new.txt").unlink()

# Traverse path
for i in Path().cwd().rglob('*.py'):
    print(i)

# Path tree
def tree(directory):
    print(f"+{directory}")
    for path in sorted(directory.rglob("*")):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        if path.is_file():
            print(f'{spacer}f {path.name}')
        else:
            print(f'{spacer}d {path.name}')

tree(path.cwd())

# Read text
path = Path("smtplib_test_file.txt")
content = path.read_text()
print(content)

# Use with PrettyTable
pt = PrettyTable()
pt.field_names = ["File Name", "Size", "Created"]
pt.align["File Name"] = "l"
pt.align["Size"] = "r"
pt.align["Created"] = "r"
for i in Path().cwd().rglob('*.py'):
    created = datetime.datetime.fromtimestamp(i.stat().st_ctime)
    size = i.stat().st_size
    pt.add_row([i.name, size, f"{created:%Y-%m-%d}"])
print(pt)