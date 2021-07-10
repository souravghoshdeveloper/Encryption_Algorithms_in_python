import hashlib
# Md5
user_input_md5 = input("Enter text here (MD5) ")
h_md5 = hashlib.md5(user_input_md5.encode())
h2_md5 = h_md5.hexdigest()
print(h2_md5)

#sha1
user_input_sha1 = input("Enter text here(SHA1) ")
h_sha1 = hashlib.sha1(user_input_sha1.encode())
h2_sha1 = h_sha1.hexdigest()
print(h2_sha1)

#sha224
user_input_sha224 = input("Enter text here(SHA224) ")
h = hashlib.sha224(user_input_sha224.encode())
h2 = h.hexdigest()
print(h2)