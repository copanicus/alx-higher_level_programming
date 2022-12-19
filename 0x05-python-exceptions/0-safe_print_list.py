#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    elements_printed = 0
    try:
        while elements_printed < x:
            print(my_list[elements_printed], end=' ')
            elements_printed += 1
    
    except IndexError:
        # IndexError is raised when trying to access an index that is out of bounds
        pass
    print()
    return elements_printed
