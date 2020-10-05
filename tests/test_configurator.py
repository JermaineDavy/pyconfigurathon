from pyconfigurathon import configurator


configurator.set_config_file('settings.json')
print(configurator.get('app_name'))
