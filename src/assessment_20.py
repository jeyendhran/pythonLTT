import os
import tarfile
from zipfile import ZipFile

file_paths = []
d = {}
for root, directories, files in os.walk("/home/cisco/PythonLTT/Git"):
    d.update(dict(zip([os.path.join(root,file) for file in files],[os.stat(os.path.join(root,file)).st_size for file in files])))


def findZerosizefiles(d):
    zero_files = []
    for file,size in d.items():
        if size == 0:
            zero_files.append(file)
    return zero_files


print("Zero size files in directory are",findZerosizefiles(d))


tarfilename = "src.tar"
tarfiles = {}
with tarfile.open(tarfilename,"r") as t:
    for files in t.getmembers():
        tarfiles[files.name] = files.size


print("Zero size files in tar file are",findZerosizefiles(tarfiles))

zipfilename = "/home/cisco/PythonLTT/Git/src.zip"
zipfiles = {}
with ZipFile(zipfilename,"r") as t:
    for files in t.infolist():
        zipfiles[files.filename] = files.file_size

print("Zero size files in zip file are",findZerosizefiles(zipfiles))
