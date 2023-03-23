import os
import logging
import configparser
from singleton_decorator import singleton


@singleton
class Configuration:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        os.makedirs(os.path.dirname(self.config["LOGS"]["ERROR"]), exist_ok=True)
        logging.basicConfig(filename=self.config["LOGS"]["ERROR"], format='%(levelname)s - %(asctime)s - %(message)s', encoding='utf-8', level=logging.INFO)
        self.sections = self.config.sections()
    
    def get(self, __name: str):
        return self.config[__name]
