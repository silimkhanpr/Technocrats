import hashlib
a = input("Enter desired string: ")
print(hashlib.sha256(a.encode('utf-8')).hexdigest())
