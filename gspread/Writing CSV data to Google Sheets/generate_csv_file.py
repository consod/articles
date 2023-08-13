from faker import Faker
import csv

fake: Faker = Faker()
Faker.seed(0)

fake_users: list = [[fake.user_name(), fake.email()] for x in range(100)]

with open("fake_users.csv", "w", encoding="UTF-8", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(fake_users)
