#include <pybind11/pybind11.h>
#include <iostream>

namespace py = pybind11;

void funcOne(){
    std::cout << "My first function for Python on C++.\n";
}


PYBIND11_MODULE(example, m) {
    
    m.def("funcOne", &funcOne, R"pbdoc(
            My first function for Python on C++.
        )pbdoc");
    
#ifdef VERSION_INFO
m.attr("__version__") = VERSION_INFO;
#else
m.attr("__version__") = "dev";
#endif
}
