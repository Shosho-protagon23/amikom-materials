import random

def generate_phone_number():
    # Mulai dengan '08'
    prefix = '08'
    # Generate 10 digit acak (total 12 digit: 08 + 10 digit)
    digits = ''.join(random.choice('0123456789') for _ in range(10))
    return prefix + digits

# Contoh penggunaan: generate satu nomor
phone_number = generate_phone_number()
print(phone_number)