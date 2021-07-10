import hashlib
user_input = input("Enter text here (MD5): ")
salt = "enteryoursalt"
textandsalt = salt + user_input
h_md5 = hashlib.md5(textandsalt.encode())
h2_md5 = h_md5.hexdigest()
print(h2_md5)