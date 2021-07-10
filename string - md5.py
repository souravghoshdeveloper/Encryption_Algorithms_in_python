import hashlib
user_input = input("Enter text here ")
h = hashlib.md5(user_input.encode())
h2 = h.hexdigest()
print(h2)