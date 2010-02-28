#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdio.h>

#define N_SYMBOLS 256

static PyObject *shannon_entropy(PyObject *self, PyObject *args);

PyDoc_STRVAR(shannon_entropy_doc, "shannon_entropy(string) -> float\n"
"\n"
"Compute the average Shannon entropy, as number of bits of data per\n"
"8-bit byte, of the given string.");

static PyObject *shannon_entropy(PyObject *self, PyObject *args) {
	uint64_t alphabet[N_SYMBOLS];
	char *buf;
	Py_ssize_t i, buflen;
	uint8_t val;
	double entropy, relfreq;

	if (!PyArg_ParseTuple(args, "t#", &buf, &buflen))
		return (NULL);

	memset(alphabet, 0, sizeof(uint64_t) * N_SYMBOLS);

	
	/* Count occurances of each 8-bit value */
	for (i = 0; i != buflen; i++) {
		val = buf[i];
		alphabet[val] += 1;
	}

	entropy = 0.0;

	for (i = 0; i < N_SYMBOLS; i++) {
		if (alphabet[i]) {
			relfreq = (double) alphabet[i] / (double) buflen;
			entropy += -relfreq * logb(relfreq);
		}
	}

	return PyFloat_FromDouble(entropy);
}

static PyMethodDef entropy_methods[] = {
	{"shannon_entropy", shannon_entropy, METH_VARARGS, shannon_entropy_doc},
	{NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC init_entropy(void) {
	(void) Py_InitModule("_entropy", entropy_methods);
}
