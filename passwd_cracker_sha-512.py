import hashlib

def testPass(cryptPass):
    dict_file='dictionary.txt'
    with open(dict_file,'r') as dictFile_obj:
        for word in dictFile_obj:
            word.encode('utf-8')
            word = word.strip()
            # create an hash obj
            obj = hashlib.sha256()
            obj.update(word)
            cryptWord = obj.hexdigest()
            print("The encrpted string of " + word + " is " + cryptWord)
            if(cryptWord == cryptPass):
                print("[+] Found Password: " + word)
                return
        print("[-] Password Not Found.")
        return

def main():
    passwd_file='passwords.txt'
    with open(passwd_file) as passwdFile_obj:
        for line in passwdFile_obj:
            if ":" in line:
                # split the line with ':' into several parts,
                # store part 0 as user
                user = line.split(':')[0]
                # the second part is the encrpted password. store it after strip
                cryptPass = line.split(':')[1].strip()
                print("[*] Cracking Password For: " + user)
                testPass(cryptPass)

if __name__ == "__main__":
    main()

