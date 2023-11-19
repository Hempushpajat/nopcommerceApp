import configparser
import os
#configparser module in Python and is used to work with configuration files in an INI file format.
# The RawConfigParser class is a basic configuration parser that preserves case sensitivity of option names and values
config= configparser.RawConfigParser()
config_file_path = os.path.abspath("../Configurations/config.ini")

config.read(config_file_path)

class readConfig:
    @staticmethod
    #     for every common info we need to create separate methods
    def getApplicationUrl():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password

