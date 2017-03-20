import hashlib

BLOCKSIZE = 65536
hasher = hashlib.md5()
with open('C:/Users/sintu/Documents/CHT.docx', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print(hasher.hexdigest())
