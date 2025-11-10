import argon2

# Declare the password as a bytes object
password = b'@Echo10Foxtrot2006#'

# Hash the password using Argon2
hashed_password = argon2.hash_password(password)

# Print the hashed password
print(hashed_password)