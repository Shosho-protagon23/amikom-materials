from faker import Faker

fake = Faker()

nama = fake.name()
alamat = fake.address()
phone = fake.phone_number()
email = fake.email()

print(nama)
print(alamat)
print(phone)
print(email)