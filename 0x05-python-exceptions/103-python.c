#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints information about a Python list object
 * @p: pointer to a PyObject
 */

void print_python_list(PyObject *p)
{
    Py_ssize_t i, size;
    PyObject *item;
    
    if (!PyList_Check(p))
    {
        printf("Error: Invalid List Object\n");
        return;
    }
    
    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    
    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, item->ob_type->tp_name);
    }
}

/**
 * print_python_bytes - prints information about a Python bytes object
 * @p: pointer to a PyObject
 */

void print_python_bytes(PyObject *p)
{
    Py_ssize_t i, size;
    char *str;
    
    if (!PyBytes_Check(p))
    {
        printf("Error: Invalid Bytes Object\n");
        return;
    }
    
    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);
    
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    printf("  first %ld bytes: ", size < 10 ? size : 10);
    
    for (i = 0; i < size && i < 10; i++)
        printf("%02hhx%c", str[i], i + 1 < size && i + 1 < 10 ? ' ' : '\n');
}

/**
 * print_python_float - prints information about a Python float object
 * @p: pointer to a PyObject
 */

void print_python_float(PyObject *p)
{
    double value;
    
    if (!PyFloat_Check(p))
    {
        printf("Error: Invalid Float Object\n");
        return;
    }
    
    value = PyFloat_AsDouble(p);
    printf("[.] float object info\n");
    printf("  value: %g\n", value);
}
