import random


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min >= max or quantity < 1 or quantity > (max - min + 1):
        return []
    number_ticket = list(range(min, max + 1))
    random_numbers = random.sample(number_ticket, quantity)
    return sorted(random_numbers)
