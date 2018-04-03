import os
from configparser import ConfigParser

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def config_setup(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    file_path = os.path.join(__location__, filename)
    parser.read(file_path)

    if parser.has_section(section):
        params = parser.items(section)
        return {param[0]: param[1] for param in params}
    else:
        raise Exception("Section '{0}' not found in file '{1}'".format(section, filename))
