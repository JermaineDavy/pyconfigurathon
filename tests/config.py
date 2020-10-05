import os
from pyconfigurathon.configurator import configurator


def get_config(config_name, file="settings.json"):
    cf = configurator(os.path.join(os.path.dirname(__file__), file))

    return cf.get(config_key=config_name)
