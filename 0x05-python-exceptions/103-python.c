#include <Python.h>

/* Function to print information about Python lists */
void print_python_list(PyObject *p) {
    Py_ssize_t size, i;

    if (!PyList_Check(p)) {
        fprintf(stderr, "[*] Python list info\n  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyObject_Length(p);
    printf("[*] Python list info\n[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

/* Function to print information about Python bytes objects */
void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;

    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyObject_Size(p);
    printf("[.] bytes object info\n  size: %ld\n", size);

    str = PyBytes_AsString(p);
    printf("  trying string: %s\n", str);

    printf("  first %d bytes: ", size < 10 ? (int)size : 10);
    for (i = 0; i < (size < 10 ? size : 10); i++) {
        printf("%02x%c", str[i] & 0xff, i == (size < 10 ? size : 10) - 1 ? '\n' : ' ');
    }
}

/* Function to print information about Python float objects */
void print_python_float(PyObject *p) {
    double val;

    if (!PyFloat_Check(p)) {
        fprintf(stderr, "[.] float object info\n  [ERROR] Invalid Float Object\n");
        return;
    }

    val = PyFloat_AsDouble(p);
    printf("[.] float object info\n  value: %f\n", val);
}
