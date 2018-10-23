'''
Create exceptions based on your inputs. Please follow the tasks below.

 - Capture and handle system exceptions
 - Create custom user-based exceptions
'''

class ExceptionHandler(Exception):
    def __init__(self, message):
        super(ExceptionHandler, self).__init__(message)
        self.message = message