import random
import string

class RandomDataGenerator:
    @staticmethod
    def generate_random_email():
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"{random_string}@gmail.com"
