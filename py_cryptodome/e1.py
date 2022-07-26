from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

salt32 = get_random_bytes(32)
print("salt", salt32)
password = "mypass"

key = PBKDF2(password, salt32, 32)  # same key can be created using same salt and password
print("key", key)
 # b'\x14\x01\xad\xc49\x0e\xfdznS\xb1e\xba\x1c\xf7\xe5\xc5\xf0\xc4\xea\xb9\xa20o\xe7!\xe5\x1339\xe7N'
msg = b"password"

cipher = AES.new(key, AES.MODE_CBC)
cipherd_data = cipher.encrypt(pad(msg, AES.block_size))
print("encrypted data:", cipherd_data)

with open("mykey.bin", "wb") as f:
    f.write(cipher.iv)
    f.write(cipherd_data)
