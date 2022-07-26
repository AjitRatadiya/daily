from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

salt32 = get_random_bytes(32)
print("salt", salt32)
password = "mypass"

key = PBKDF2(password, salt32, 32)  # same key can be created using same salt and password
print("key", key)


with open("mykey.bin", "rb") as f:
    iv = f.read(16)
    safe_data =f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original_data = unpad(cipher.decrypt(safe_data),AES.block_size)

print("original :", original_data)
