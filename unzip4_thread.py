# import thread to polish up the performance
import zipfile
from threading import Thread

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd = password.encode(encoding = 'utf-8'))
        print('[+] Found password ' + password)
    except:
        pass

def main():
    zFile = zipfile.ZipFile("evil.zip")
    with open('dictionary.txt','r') as passFile:
        lines = passFile.readlines()
    for line in lines:
        password = line.strip()
        t = Thread(target = extractFile, args = (zFile, password))
        t.start()

if __name__ == '__main__':
    main()
