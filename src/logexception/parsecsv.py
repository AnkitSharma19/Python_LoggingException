# Error & Exception handling
import os
import logging
from src.logexception.exceptionhandler import ExceptionHandler


def parse_csv_and_get_columns(filename):

    try:
        logger = logging.getLogger('my_module')
        if(os.path.exists(filename)):
            csvFile = open(filename, 'r')
            lines = csvFile.readlines()
            for line in lines[1:]:
                val = line.split(",")
                test_str_div = val[0] / val[11]

        else:
            logging.info('File not found')
            ExceptionHandler()

    except IOError:
        logger.error('IO Error | An error occurred trying to read the file.')

    except Exception as ex:
        logger.error('TypeErrorException |  Please check the operands type')
        raise ExceptionHandler(' |  Please check the operands type')

    except Exception as ex:
        logger.error('OtherException | Incorrect value or type error.')

if __name__ == "__main__":
    parse_csv_and_get_columns(filename="data/flights.csv")