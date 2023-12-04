#include <Python.h>

void print_python_list_info(PyObject *p)
{
    if (PyList_Check(p)) {
        Py_ssize_t count;
        Py_ssize_t length = PyList_Size(p);
        PyListObject *pObj = (PyListObject *)p;

        printf("[*] Size of the Python List = %zd\n", length);
        printf("[*] Allocated = %zd\n", pObj->allocated);

        for (count = 0; count < length; count++) {
            // Access elements directly using pObj->ob_item[count]
            printf("Element %zd: %s\n", count, Py_TYPE(pObj->ob_item[count])->tp_name);
        }
    } else {
        printf("Error: Not a Python list object\n");
    }
}

