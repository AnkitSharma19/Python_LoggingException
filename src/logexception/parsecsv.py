# Error & Exception handling

from src.logexception.exceptionhandler import ValueErrorException
import src.logexception.logframework


def parse_csv_and_get_columns(filename):
    count = 0
    try:
        csvFile = open(filename, 'r')
        lines = csvFile.readlines()
        for line in lines[1:]:
            val = line.split(",")
            test_str_div = val[0] / val[11]

    except IOError:
        print('IO Error | An error occurred trying to read the file.')

    except ValueErrorException:
        print('ValueErrorException | Non-numeric data found in the file.')

    except TypeError:
        print('TypeErrorException | Please check the operands type')



if __name__ == "__main__":
    parse_csv_and_get_columns(filename="data/flights.csv")
