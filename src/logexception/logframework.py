'''
Create a logging framework to collect all the logs into a single file .Please follow all the tasks below.

 - Make the logger customisable, with settings being retrieved from a configuration file
 - Create the logging framework; every time the logger is invoked, it should log into a single file
 - The logging format has to be generic with the module_name, function_name, line_no : message
'''

# from functools import wraps

import logging.config
import logging

class CustomLogging:
    def ApplicationExceptionLog(self):
        logger = logging.getLogger(__name__)
        logger.info('Application Exception')

    def ValueErrorLog(self):
        logger = logging.getLogger(__name__)
        logger.info('Value Exception Log')

    def TypeErrorLog(self):
        logger = logging.getLogger(__name__)
        logger.info('Value Exception Log')


    class ExceptionLog(object):
        def __init__(self, logger=None):
            self.logger = logger or logging.getLogger(__name__)

        def ExceptionLog(self):
            self.logger.info('Exception Log')

    # custom = yaml.load(open('config.yaml', 'r'))
    # logging.config.dictConfig()



    # def __init__(self, name, time, filename,functionname):
    #     self.name = ''
    #     self.time = ''
    #     self.filename = ''
    #     self.functionname = ''
    #
    # def my_logging(orig_func):
    #     import logging
    #     logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    #     @wraps(orig_func)
    #     def wrapper(*args, **kwargs):
    #         logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs) )
    #         return orig_func(*args, **kwargs)
    #     return wrapper
    #
    #
    # # Logging time function
    # def my_timer(orig_func):
    #     import time
    #     @wraps(orig_func)
    #     def wrapper(*args, **kwargs):
    #         t1 = time.time()
    #         result = orig_func(*args, **kwargs)
    #         t2 = time.time() - t1
    #         print('{} ran in: {} sec\n\n'.format(orig_func.__name__, t2))
    #         return result
    #     return wrapper
