# Mike Brian Olivera

import glob, os, sys
from os.path import basename
carpeta = sys.argv[1]
path=os.path.join(os.getcwd(),carpeta)
print path
os.chdir(path)
for file in glob.glob("*.vtt"):
    name= ".".join(file.split(".")[:-1])
    with open(file, 'r') as fin:
        data = fin.read().splitlines(True)
    os.remove(file)
    with open(name+ ".srt", 'w') as fout:
        fout.writelines(data[1:])