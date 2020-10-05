import json


class configurator:
    #   Placeholder for the path to the configuration file.
    __config_file = None

    #   Sets the path to the configuration file.
    #
    #   @param file_path - The path to the config file
    def __init__(self, file_path):
        self.__config_file = file_path

    #   Gets a single value from the configuration file.
    #
    #   The key to the value should be the name of the key. If the value is nested within the JSON, then the name of
    #   each key should be separated by a period. Eg. "db.mysql.host" or "credentials.username"
    #
    #   @param config_key - The key to the configuration value you want to retrieve.
    #   @return The value of the provided key.
    def get(self, config_key):
        if self.__config_file is None:
            raise Exception('No configuration file provided.')

        if not self.__config_file.endswith('.json'):
            raise Exception('Invalid file type. Please select a valid JSON file.')

        config_parts = config_key.split('.')

        with open(self.__config_file) as settings_file:
            settings = json.load(settings_file)

            #   Loops through each nested value of the key until the the last nested value. At the end each of each
            #   loop, the initial value is replaced by the nested value. The last value found is the value which has
            #   been requested.
            for part in config_parts:
                #   If the current part if the key is not a value in the remaining part of the nest, then a check is
                #   perform to check if the key is actually an index. If it is an index but isn't an index of the
                #   current nested value, then an exception saying so is raised.
                #
                #   If the key part is not a number then an exception will be raised for a missing value.
                if part not in settings:
                    if part.isnumeric():
                        if int(part) > (len(settings) - 1):
                            raise Exception('"{}" contains an index not defined in the configuration\
                            file'.format(config_key))
                    else:
                        raise Exception('"{}" is not within the selected configuration file.'.format(config_key))

                #   This value gets replaced at the end of each loop with the following nested value unless there are no
                #   more nest to loop through, in which case the final value is set.
                settings = settings[int(part)] if part.isnumeric() else settings[part]

            #   Returns the value requested.
            return settings
