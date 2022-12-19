def safe_print_integer(value):

    try:

        # Try to print the integer using "{:d}".format()

        print("{:d}".format(value))

        # If the above line doesn't throw an exception, it means the value is an integer

        # So, return True

        return True

    except ValueError:

        # If the above line throws a ValueError exception, it means the value is not an integer

        # So, return False

        return False
