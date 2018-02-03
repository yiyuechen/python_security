# reconsitution of unzip2.py
import zipfile

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd = password.encode(encoding = 'utf-8'))
        return password
    except:
        return

def main():
    zFile = zipfile.ZipFile("evil.zip")
    with open('dictionary.txt','r') as passFile:
        lines = passFile.readlines()
    for line in lines:
        password = line.strip()
        guess = extractFile(zFile, password)
        if guess:
            print('[+] Password = ' + password)
            exit(0)

if __name__ == '__main__':
    main()
