import random
import string

def random_character():
    return random.choice(string.ascii_letters)


def random_alphabetical_string(length=None):
    if length is None:
        length=random.randint(1,100)
    return ''.join(random.choice(string.ascii_letters)for _ in range(length))

print(random_character())
print(random_alphabetical_string())
print(random_alphabetical_string(10))


