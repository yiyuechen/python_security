import zipfile
zFile = zipfile.ZipFile("evil.zip")
try:
    pss = b"secreta"
    zFile.extractall(pwd=pss)
except RuntimeError as e:
    print(e)
