import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    special_chars = list(allowed_special_chars)
    generate_id = []
    for i in range(number_of_small_letters):
        small_letters = random.choice(string.ascii_lowercase)
        generate_id.append(small_letters)
    for i in range(number_of_capital_letters):
        capital_letters = random.choice(string.ascii_uppercase)
        generate_id.append(capital_letters)
    for i in range(number_of_digits):
        digits = random.randint(0, 9)
        generate_id.append(str(digits))
    for i in range(number_of_special_chars):
        chars = random.choice(special_chars)
        generate_id.append(chars)
    random.shuffle(generate_id)
    generate_id = "".join(generate_id)
    return generate_id
