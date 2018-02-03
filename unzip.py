import zipfile
zFile = zipfile.ZipFile("evil.zip")
pss = b"secret"
zFile.extractall(pwd=pss)
