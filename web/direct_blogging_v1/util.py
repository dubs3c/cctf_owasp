import hashlib

def secure_md5_hashing(password):
    m = hashlib.md5()
    m.update(password.encode())
    return m.hexdigest()
