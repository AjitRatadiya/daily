from cryptography.fernet import Fernet

msg = b"gAAAAABimfun77PdQIUkSzVI1jKFyqEM8xywQ7eL2CGlJ063T_6kxJfDtRTi-tZl6-_WdKcnAxztJdp62zrJyZIegB7Obj_4BA=="

# key = Fernet.generate_key()
# print(key)

dek = Fernet(b'-vSjjoHRH7sQDu7w9tltdTjQ6EiMOUmoY2SzFaCY4ls=')

en = dek.decrypt(msg)
print(type(en), en)

str = en.decode()

print(type(str), str)

