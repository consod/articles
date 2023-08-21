import csv
from pprint import pprint
from faker import Faker

fake = Faker()

first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
user_name = fake.user_name()

# print(fake.first_name(), fake.last_name(), fake.email(), fake.user_name())

users = [[fake.first_name(), fake.last_name(), fake.email(), fake.user_name()] for x in range(50)]

#pprint(users)

with open("users.csv", "w", encoding="UTF-8", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(users)
