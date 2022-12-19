import sys



def safe_function(fct, *args):

  try:

    # Call the function with the given arguments

    return fct(*args)

  except Exception as e:

    # Print the exception message to stderr

    print("Exception:", e, file=sys.stderr)

    # Return None

    return None
