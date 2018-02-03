import crypt
def testPass(cryptPass):
    salt = cryptPass[0:2]
    dict_file='dictionary.txt'
    with open(dict_file,'r') as dictFile_obj:
        for word in dictFile_obj:
            word = word.strip()
            cryptWord = crypt.crypt(word, salt)
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

