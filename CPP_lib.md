## Создание библиотеки для Питона из кода на С++

Как создать из кода на C++ библиотеку для Python?  
**_Вариант 1._** CPython, но о нем в следующий раз  
**_Вариант 2._** С помощью библиотеки PyBind11  

### PyBind11
1. Скачать библиотеку PyBind11 с помощью команды в командной строке:  
`pip install pybind11`  
   
   Или склонировать репозиторий с сайта и самостоятельно собрать библиотеку   
<https://github.com/pybind/pybind11>  

   Если возникнут проблемы с установкой советую взглянуть  
<https://pybind11.readthedocs.io/en/latest/installing.html>  
Или написать мне :)
  
2. Написать код библиотеки на С++ (см. example.cpp)
```cpp
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
```
  Где ```#include <pybind11/pybind11.h>``` - подключение библиотеки, коорую мы на предыдущем шаге устанавливали.   
  ```funcOne()``` - функция, которую мы будем вызывать в Python из нашей библиотеки.
  Наша первая функция не будет ничего делать, кроме вывода в консоль текста "My first function for Python on C++."

3. Собрать библиотеку  
  Для этого мы будем использовать файл _setup.py_. Он содержит в себе инструкции по сборке библиотеки:
  ```python
  import os, sys

from distutils.core import setup, Extension
from distutils import sysconfig

cpp_args = ['-std=c++11', '-stdlib=libc++', '-mmacosx-version-min=10.7']

sfc_module = Extension(
    'example', sources = ['example.cpp'],
    include_dirs=['pybind11/include'],
    language='c++',
    extra_compile_args = cpp_args,
    )

setup(
    name = 'example',
    version = '1.0',
    description = 'Python package with C++ extension (PyBind11)',
    ext_modules = [sfc_module],
)
```
  Пока не будем разбираться в его содержании...  
  Для того чтобы собрать библиотеку необхожимо записать в консоли команду ```pip install . ```.   
  Важно, что вы до этого должны пописать в консоли путь к папке содержащей файл _setup.py_, в этой же папке должен содержаться _example.cpp_.  
  Если сборка прошла успешно, переходим к следующему пункту.

4. Код на Python
  Приведу простейший пример кода на Python, который только вызывает нашу функцию из С++.
  ```python
  import example as lib 

  lib.funcOne()
  ```
  Если у вас все получилось, то в консоль выведется фраза "_My first function for Python on C++._". **Поздравляю!**
  
  
  
  
