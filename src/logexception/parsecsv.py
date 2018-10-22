# Error & Exception handling

from src.logexception.exceptionhandler import ValueErrorException
import logging
from src.logexception.logframework import CustomLogging
import yaml

# @my_logging
# @my_timer
def parse_csv_and_get_columns(filename):

    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
        logger = logging.getLogger(__name__)
        # logging.debug('error message')

    count = 0
    try:
        csvFile = open(filename, 'r')
        lines = csvFile.readlines()
        for line in lines[1:]:
            val = line.split(",")
            test_str_div = val[0] / val[11]

    except IOError:
        CustomLogging.ApplicationExceptionLog('IO Error | An error occurred trying to read the file.')

    except ValueErrorException:
        CustomLogging.ValueErrorLog('ValueErrorException | Non-numeric data found in the file.')

    except TypeError:
        CustomLogging.TypeErrorLog('TypeErrorException | Please check the operands type')

if __name__ == "__main__":
    parse_csv_and_get_columns(filename="data/flights.csv")
