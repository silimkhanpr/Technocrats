import hashlib

def sha_hash():
    BLOCKSIZE = 65536
    hasher = hashlib.sha256()
    obj = open("test.txt", "rb")
    buf = obj.read(BLOCKSIZE) 
    while len(buf) > 0:
            hasher.update(buf)
            buf = obj.read(BLOCKSIZE)
    a = hasher.hexdigest()

    #print (type(a))
    print("The hash is:", a)
    return 
