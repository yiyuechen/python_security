import crypt
passwd="egg"
encrypted_passwd=crypt.crypt(passwd,"HX")
print(encrypted_passwd)

