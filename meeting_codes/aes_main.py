from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad

salt = get_random_bytes(32)
password = "pass123"

key = PBKDF2(password,salt, dkLen=32)

# print(key)

message = "This is my message"

cipher = AES.new(key,AES.MODE_CBC)

ciphered_data = cipher.encrypt(pad(message.encode(),AES.block_size))

# print(ciphered_data)

with open("cipher.bin","wb") as f:
    f.write(cipher.iv)
    f.write(ciphered_data)

with open("cipher.bin", "rb") as f:
    iv = f.read(16)
    cipher_data = f.read()

cipher = AES.new(key,AES.MODE_CBC, iv=iv)
original_message = unpad(cipher.decrypt(cipher_data),AES.block_size)

print(original_message.decode())

