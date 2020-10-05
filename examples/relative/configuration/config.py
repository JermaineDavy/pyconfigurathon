import os
from pyconfigurathon.configurator import configurator


#   In this example, a path relative to this script(config.py) is provided. If you decide to follow the relative route,
#   when providing file names, you would have to use the following examples as a reference:
#       - example.json => for files in the same directory
#       - dir_name/settings.json => for files in sub directories
#       - ../config.json => for files in parent directories
#
#   @param config_name - The name/key of the configuration which should be retrieved from the file.
#   @param file - The relative path to the file containing the configuration.
#
def get_config(config_name, file="settings.json"):
    conf = configurator(os.path.join(os.path.dirname(__file__), file))

    return conf.get(config_key=config_name)
