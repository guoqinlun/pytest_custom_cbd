import random
import string

from faker.providers import BaseProvider


class CustomProvider(BaseProvider):
    def mouse(self):
        self.mouse_brand_list = ['罗技', '苹果']
        brand = ''.join(random.choices(self.mouse_brand_list))
        all_characters_and_digits = string.ascii_letters + string.digits
        number = ''.join(random.choices(all_characters_and_digits, k=5))
        return f'{brand}-{number}'
