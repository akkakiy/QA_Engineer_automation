from faker import Faker

fake = Faker('ru_RU')


class MainUser:
    NAME_USER = 'Maximus'
    EMAIL_USER = 'kagorta_07@gmail.com'
    PASS_USER = 'Zaq12wsxcde34rfv'


class RandomUser:
    NAME_RANDOM_USER = fake.name()
    EMAIL_RANDOM_USER = fake.email()
    PASS_RANDOM_USER = fake.password()
