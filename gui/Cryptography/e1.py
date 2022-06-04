from cryptography.fernet import Fernet

msg = b"i_am_ajit"

token = Fernet.generate_key()
print(token)

dek = Fernet(token)
de = dek.encrypt(msg)
print(de)

en = dek.decrypt(de)
print(type(en), en)

str = en.decode()

print(type(str), str)

