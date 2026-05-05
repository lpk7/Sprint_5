import random


def email():
    email = f"{random.randint(1, 1000)}@{random.randint(1, 1000)}.ru"
    return email


def password():
    new_pass = random.randint(100, 10000)
    return new_pass


def price():
    price = random.randint(20000, 55000)
    return price
