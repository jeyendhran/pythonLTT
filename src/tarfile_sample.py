import tarfile
import os

for filename in ['README.txt', 'src.tar',
                 'bad_example.tar', 'notthere.tar']:
    try:
        print('{:>15}  {}'.format(filename, tarfile.is_tarfile(
            filename)))
    except IOError as err:
        print('{:>15}  {}'.format(filename, err))


with tarfile.open('src.tar', 'r') as t:
    print(t.getnames())

import time

with tarfile.open('src.tar', 'r') as t:
    for member_info in t.getmembers():
        print(member_info.name)
        print('  Modified:', time.ctime(member_info.mtime))
        print('  Mode    :', oct(member_info.mode))
        print('  Type    :', member_info.type)
        print('  Size    :', member_info.size, 'bytes')

os.mkdir('outdir')
with tarfile.open('src.tar', 'r') as t:
    t.extractall('outdir')
print(os.listdir('outdir'))