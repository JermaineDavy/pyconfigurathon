#   PyConfigurathon

A python package for making it easy to use and manage configuration files in your python applications.

## Installation

#### Using poetry
    `poetry add pyconfigurathon`

#### Using pip
    `pip install pyconfigurathon`


## How to use

The recommended way to use this module is to have a module dedicated to your configuration. Eg. config.py

### Use with an absolute path to the configuration file:
```
from pyconfigurathon.configurator import configurator


def get_config(config_name, file_path="/path/to/file/settings.json"):
    cf = configurator(file_path)

    return cf.get(config_key=config_name)
```

### Use with a path to the configuration file relative to the config.py file
```
import os
from pyconfigurathon.configurator import configurator


def get_config(config_name, file="settings.json"):
    conf = configurator(os.path.join(os.path.dirname(__file__), file))

    return conf.get(config_key=config_name)
```

Please note that these are only examples to help you get started faster. There are other ways to use this package.