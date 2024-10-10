from faker import Faker


class DataGenerator:
    def __init__(self):
        self.fake = Faker('zh_CN')

    def generate_name(self):
        #  """
        # ����������֡�
        #  """
        return self.fake.name()

    def generate_address(self):
        #  """
        # ���������ַ��
        #  """
        return self.fake.address()

    def generate_phone_number(self):
        # """
        # ��������绰���롣
        # """
        return self.fake.phone_number()

    def generate_email(self):
        # """
        # ������������ַ��
        # """
        return self.fake.email()

    def generate_company_name(self):
        # """
        # ���������˾���ơ�
        # """
        return self.fake.company()

    def generate_date(self):
        # """
        # ����������ڡ�
        # """
        return self.fake.date()

    def generate_ip(self):
        return self.fake.ipv4()
