'''
Create a logging framework to collect all the logs into a single file .Please follow all the tasks below.

 - Make the logger customisable, with settings being retrieved from a configuration file
 - Create the logging framework; every time the logger is invoked, it should log into a single file
 - The logging format has to be generic with the module_name, function_name, line_no : message
'''
import os
import logging.config
from src.logexception.exceptionhandler import ExceptionHandler
import yaml

class LogFramework():
    def logger(self):
        log_level = logging.INFO
        path_config = os.path.dirname('config.yaml')
        print(path_config)

        if os.path.exists(path_config):
            with open(path_config,'rt') as e:
                config = yaml.safe_load(e.read())

                logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=log_level)

        return logging
