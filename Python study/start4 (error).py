import hashlib
import base64
import uuid

password = "Passwordtest"
salt = base64.urlsafe_b64decode(uuid.uuid4().bytes)

t_sha = hashlib.sha512()
t_sha.update(password + salt)
hashed_password = base64.urlsafe_b64decode(t_sha.digest())