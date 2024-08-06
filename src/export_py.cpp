//
// Created by aichao on 2024/7/12.
//

#include "config.h"
#include "MyLibrary.h"
#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(PY_MODULE_NAME, m) {
    py::class_<Base>(m, "Base")
            .def(py::init<int>())
            .def("get_x", &Base::get_x);


    py::class_<MyLibrary, Base>(m, "MyLibrary")
            .def(py::init<int, int>())
            .def("add", &MyLibrary::add)
            .def("sub", &MyLibrary::sub)
            .def("say_hi", &MyLibrary::say_hi)
            .def("get_y", &MyLibrary::get_y)
            .def_property("name", &MyLibrary::get_name, &MyLibrary::set_name);
}
