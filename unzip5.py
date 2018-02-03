# identify zip file name and dictionary name

import zipfile
import optparse
from threading import Thread

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd = password.encode(encoding = 'utf-8'))
        print('[+] Found password ' + password)
    except:
        pass

def main():
    parser = optparse.OptionParser(usage = "%prog -f <zipfile> -d <dictionary>", version = "%prog v0.1")
    parser.add_option('-f', dest = 'zname', type = 'string', help = 'specify zip file')
    parser.add_option('-d', dest = 'dname', type = 'string', help = 'specify dictionary file')
    (options, args) = parser.parse_args()
    if(options.zname == None) | (options.dname == None):
        print(parser.usage)
        exit()
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    with open(dname,'r') as passFile:
        lines = passFile.readlines()
    for line in lines:
        password = line.strip()
        t = Thread(target = extractFile, args = (zFile, password))
        t.start()

if __name__ == '__main__':
    main()
