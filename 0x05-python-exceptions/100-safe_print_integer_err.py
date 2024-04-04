#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Prints an integer with error handling."""
    try:
        print("{:d}".format(value))
        return True
    except TypeError:
        type_str = str(type(value)).split("'")[1]
        error_msg = "Exception:Unknown format code 'd' for object of type '{}'"
        error_msg = error_msg.format(type_str)
        print(error_msg, file=sys.stderr)
        return False


if __name__ == "__main__":
    value = 89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "School"
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))
