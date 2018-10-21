
'''
Create exceptions based on your inputs. Please follow the tasks below.

 - Capture and handle system exceptions
 - Create custom user-based exceptions
'''


class CustomInputError(Exception):
    pass

class ValueErrorException(CustomInputError):
    pass

class IOError(CustomInputError):
    pass

class TypeError(CustomInputError):
    pass
