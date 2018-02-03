import zipfile
zFile = zipfile.ZipFile("evil.zip")
with open('dictionary.txt','r') as passFile:
    lines = passFile.readlines()
for line in lines:
    password = line.strip()
    password = password.encode(encoding = "utf-8")
    try:
        zFile.extractall(pwd = password)
        password = password.decode(encoding = "utf-8")
        # or more simple as below:
        # password = password.decode()
        print('[+] Password = ' + password)
    except RuntimeError as e:
        # print(e) 
        # do nothing instead of printing error message
        pass
