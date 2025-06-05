"""
This is the doc string for the module/script.
"""
import sys

# standard library
# third-party
# local
# current project

# constants (AKA global variables -- keep these to a minimum)
FILE_NAME = "wombats.txt"

# main function
def main(args):
    """
    This is the docstring for the main() function

    :param args: Command line arguments.
    :return: None
    """
    function1()

# other functions
def function1():
    """
    This is the docstring for function1().

    :return: None
    """
    print("this is function1()")

main(sys.argv[1:])  # Pass command line args (minus script name) to main()
