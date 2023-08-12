from faker import Faker  # pip install Faker
from pprint import pprint
from faker_education import SchoolProvider  # pip install faker_education

fake = Faker()
fake.seed_instance(0)
# print(fake.name())

# # Produces the same output
# fake1 = Faker()
# fake1.seed_instance(0)
# fake2 = Faker()
# fake2.seed_instance(0)
# # print(fake1.name())
# # print(fake2.name())

# # Does not produce the same output!
# fake3 = Faker()
# Faker.seed(0)
# fake4 = Faker()
# Faker.seed(0)
# # print(fake3.name())
# # print(fake4.name())

# Standard providers

fake_users = [[fake.user_name(), fake.email()] for x in range(10)]
# pprint(fake_users)

fake_persons = [
    [fake.name(), fake.address(), fake.postcode(), fake.city(), fake.country()]
    for x in range(5)
]
# pprint(fake_persons)

fake_finland = Faker(["fi-FI"])
fake_finland.seed_instance(0)

fake_persons_in_finland = [
    [
        fake_finland.name(),
        fake_finland.street_address(),
        fake_finland.postcode(),
        fake_finland.city(),
        fake_finland.current_country(),
        fake_finland.phone_number(),
        fake_finland.ssn(),
    ]
    for x in range(5)
]
# pprint(fake_persons_in_finland)

finnish_workers = [
    [
        fake_finland.prefix_nonbinary(),
        fake_finland.first_name(),
        fake_finland.last_name(),
        fake_finland.job(),
    ]
    for x in range(5)
]

# pprint(finnish_workers)

fake_fi_sv = Faker(["fi-FI", "sv_SE"])
fake_fi_sv.seed_instance(0)
finnish_and_swedish_names = [
    [
        fake_fi_sv.name(),
    ]
    for x in range(10)
]

# pprint(finnish_and_swedish_names)

# Community Providers
# Note that Faker.seed_instance() does not work with Community Providers
fake_education = Faker()
fake_education.add_provider(SchoolProvider)
fake_education.seed_instance(0)
print(fake_education.school_name())
print(fake_education.school_level())
