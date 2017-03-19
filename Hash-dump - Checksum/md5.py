import hashlib
a = input("Enter desired string: ")
print(hashlib.md5(a.encode('utf-8')).hexdigest())
