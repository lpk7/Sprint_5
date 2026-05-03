import pytest
from selenium import webdriver
import random


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    return driver


@pytest.fixture(scope="function")
def email():
    email = f"{random.randint(1, 1000)}@{random.randint(1, 1000)}.ru"
    return email


@pytest.fixture(scope="function")
def password():
    new_pass = random.randint(100, 10000)
    return new_pass


@pytest.fixture(scope="function")
def price():
    price = random.randint(20000, 55000)
    return price
