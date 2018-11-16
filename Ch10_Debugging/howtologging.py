#! Python3
# Print() states in your to output variable value while your programs is running is a form of logging to debug code.
# Logging is a great way to understand what is happening in your program and in what order its happening
# logging module makes it easy to create custom messages that your write and will describe execution

import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))
logging.debug('End of Program')