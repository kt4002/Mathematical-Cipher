import rsa

public_key, private_key = rsa.newkeys(1024)

# print(f"public key: {public_key}")
# print("\n")
# print(f"private key: {private_key}")

# with open("public_key.pem", "wb") as f:
#     f.write(public_key.save_pkcs1("PEM"))


# with open("private_key.pem", "wb") as f:
#     f.write(private_key.save_pkcs1("PEM"))

with open("private_key.pem", "rb") as f:
    private_key= rsa.PrivateKey.load_pkcs1(f.read())

with open("public_key.pem", "rb") as f:
    public_key= rsa.PublicKey.load_pkcs1(f.read())

message = "Hello World"

# encrypted_message = rsa.encrypt(message.encode(),public_key)

# with open("encrypted.message" , "wb") as f:
#     f.write(encrypted_message)

# encrypted_message = open("encrypted.message", "rb").read()

# decrypt_message = rsa.decrypt(encrypted_message,private_key)

# print(decrypt_message.decode())

# signature = rsa.sign(message.encode(),private_key, "SHA-256")

# with open("signature" , "wb") as f:
#     f.write(signature)

with open("signature" ,"rb") as f:
    signature = f.read()

# public_key , private_key = rsa.newkeys(1024)

print(rsa.verify(message.encode(),signature,public_key))