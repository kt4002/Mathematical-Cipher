import hashlib

# print(hashlib.algorithms_available)
# print(hashlib.algorithms_guaranteed)
# message = "hello124"
h = hashlib.new("sha256")
# h.update(message.encode())
# print(h.digest())
# print(h.hexdigest())

password = "password1234"

h.update(password.encode())

password_hash = h.hexdigest()

print(password_hash)

user_pass= "password1234"

h = hashlib.new("sha256")
h.update(user_pass.encode())
print(h.hexdigest())