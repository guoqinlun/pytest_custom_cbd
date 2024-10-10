import yaml


def read_yaml_value(file_path):
    with open(file_path,'r') as file:
        data = yaml.safe_load(file)
        return data