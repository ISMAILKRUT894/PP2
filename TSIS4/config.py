from configparser import ConfigParser

def load_config(filename='/Users/ismailkrut/PP2-1/TSIS4/database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    config = {}
    if parser.has_section(section):
        for param in parser.items(section):
            config[param[0]] = param[1]
    else:
        raise Exception("DB config not found")

    return config