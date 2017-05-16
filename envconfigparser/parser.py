from configparser import ConfigParser
import os

class EnvConfigParser(ConfigParser):
    def __getitem__(self, key):
        """ Update configuration fields in config from environment variables.

        The environment variable names are expected to be of the form, that the
        section name and the variable name are seperated by a dubble underscore,
        e.g.

            SECTION_NAME__VARIABLE_NAME

        """
        section_dict = super().__getitem__(key)
        for env_key, env_val in os.environ.items():
            if '__' in env_key:
                section, section_key = env_key.lower().split('__')
                if section == key:
                    print('Updated key')
                    section_dict[section_key] = env_val
        return section_dict
