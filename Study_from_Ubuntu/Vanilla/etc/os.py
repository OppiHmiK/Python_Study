import os

dir = os.getcwd()
print(dir)

ch_dir = os.chdir("/home/kimhippo/바탕화면/AI")
dir2 = os.getcwd()
print(dir2)

lis_or = os.listdir(os.getcwd())
print(lis_or)

for rep in lis_or:
    print(rep)

os.chdir("/home/kimhippo/바탕화면/AI/Python practice")

is_dir = os.path.isdir("/home/kimhippo/바탕화면/AI/Python practice")
print(is_dir)

is_file = os.path.isfile("/home/kimhippo/바탕화면/AI/Python practice/os.py")
print(is_file)

exist_dirfile = os.path.exists("/home/kimhippo/바탕화면/AI/Python practice/os.py")
print(exist_dirfile)

size = os.path.getsize("/home/kimhippo/바탕화면/AI/Python practice/os.py")
print(size)
size2 = os.path.getsize("/home/kimhippo/바탕화면/AI/Python practice/bs4.py")
print(size2)

split = os.path.split("/home/kimhippo/바탕화면/AI/Python practice/bs4.py")
print(split)

join = os.path.join(split[0], split[1])
print(join)

dirname = os.path.dirname("/home/kimhippo/바탕화면/AI/Python practice/os.py")
basename = os.path.dirname("/home/kimhippo/바탕화면/AI/Python practice/os.py")
print(dirname)
print(basename)
