//
// Created by aichao on 2024/7/12.
//

#include "config.h"
#include "MyLibrary.h"
#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(PY_MODULE_NAME, m) {

    py::class_<MyLibrary>(m, "MyLibrary")
            .def(py::init<>())
            .def("add", &MyLibrary::add)
            .def("sub", &MyLibrary::sub);

}
