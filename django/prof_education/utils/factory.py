import random
import string


def random_digits(k):
    return "".join(random.choices(string.digits, k=k))


def random_bool():
    return random.choice([True, False])


def choice_with_chance(chance, choice, another=None):
    # шанс выпадения — 1/chance
    k = random.randint(0, chance - 1)
    if k == 0:
        return choice() if callable(choice) else choice
    return another
