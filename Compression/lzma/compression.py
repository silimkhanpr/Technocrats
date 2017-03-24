try:
    import pylzma as lzma
except ImportError:
    import lzma
f = open("Learning Python, 5th Edition.pdf", "rb")
data = f.read()
with lzma.open("file.xz", "wb") as f:
	f.write(lzma.compress(data))
