import yaml


def read_yaml_file(yaml_file):
    with open(yaml_file) as f:
        return yaml.load(f.read())
