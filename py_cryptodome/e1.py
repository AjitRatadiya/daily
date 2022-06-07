from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

salt32 = get_random_bytes(32)
salt64 = get_random_bytes(64)
print("salt", salt32)
print("salt64:", salt64)
password = "mypass"

key = PBKDF2(password, salt32, 32)  # same key can be created using same salt and password
print("key", key)

msg = b"mypassword"

cipher = AES.new(key, AES.MODE_CBC)
cipherd_data = cipher.encrypt(pad(msg, AES.block_size))
print("encrypted data:", cipherd_data)

with open("mykey.bin", "wb") as f:
    f.write(cipher.iv)
    f.write(cipherd_data)

with open("mykey.bin", "rb") as f:
    iv = f.read(16)
    safe_data =f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original_data = unpad(cipher.decrypt(safe_data),AES.block_size)

print("original :", original_data)