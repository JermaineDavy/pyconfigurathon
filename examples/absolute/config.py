from pyconfigurathon.configurator import configurator


#   In this example the configuration file is provided with an absolute path. In the case of using absolute paths,this
#   file is not necessary as the absolute path can be provided in many ways to the configurator package. This does
#   however, help a bit with keeping your code DRY
#
#   Replace "/path/to/file/settings.json" with the actual path to your configuration file.
#
#   @param config_name - The name/key of the configuration which should be retrieved from the file.
#   @param(Optional) - The absolute path to the file containing the configuration.
def get_config(config_name, file_path="/path/to/file/settings.json"):
    cf = configurator(file_path)

    return cf.get(config_key=config_name)
