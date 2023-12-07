#include <Python.h>

void print_python_bytes(PyObject *p) {
  Py_ssize_t size, i;

  if (!PyBytes_Check(p)) {
    printf("%s is not a byte object\n", Py_TYPE(p)->tp_name);
    return;
  }

  size = PyBytes_GET_SIZE(p);
  printf("[*] Bytes at %p\n", p);
  printf("Size of the bytes: %zd\n", size);

  printf("Trying to print first %d bytes:\n", size > 10 ? 10 : size);
  for (i = 0; i < size && i < 10; ++i) {
    printf("%02x ", (unsigned char) PyBytes_AS_STRING(p)[i]);
  }

  if (size > 10) {
    printf("...");
  }

  printf("\n\n");
}
