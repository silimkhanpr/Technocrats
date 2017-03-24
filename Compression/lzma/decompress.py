try:
    import pylzma as lzma
except ImportError:
    import lzma
with lzma.open('file.xz') as f:
	data = f.read()
with open("new.pdf", "wb") as p:
	p.write(lzma.decompress(data))
