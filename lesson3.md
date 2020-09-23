# Работа с текстовыми файлами в С++

Для работы с текстовыми файлами необходимо подключить следующие библиотеки:  
    `<fstream>` - для чтения и записи тексовых файлов.  
    `<iostream>` - для работы потоками ввода-вывода.  

По аналогии с потоками `cin` и `cout` в `<fstream>` имеются потоки `ifstream` и `ofstream`, отвечающие за ввод и вывод, но не на экран, а в текстовый файл.

Для записи в файл необходимо сделать следующие шаги:  
1. создать объект класса ofstream;  
2. связать переменную с файлом, в который будет производиться запись;  
3. записать строки в файл;  
4. **закрыть файл!**

Пример:
v1  
```cpp
    #include <iostream> // для работы с текстовыми потоками
    #include <fstream>  // для работы с текстовыми файлами  
    int main(){
        std::ofstream file;                 // создаем объект класса 
        file.open("ourText.txt");           // открываем файл ourText.txt
        file << "Here we write our text.";  // записываем строку
        file.close();                       // закрываем файл
        return 0;
    }
```
v2  
```cpp
    #include <iostream> // для работы с текстовыми потоками
    #include <fstream>  // для работы с текстовыми файлами 
    int main(){
        std::ofstream file("ourText.txt");  // создаем объект класса и открываем файл ourText.txt
        file << "Here we write our text.";  // записываем строку
        file.close();                       // закрываем файл
        return 0;
    }
```

Если файла не существует, он будет создан, если существует - перезаписан.

Для того, чтобы считать файл необходимо сделать следующие шаги:  
1. создать объект класса ifstream;  
2. связать переменную с файлом, в который будет производиться запись;  
3. прочитать файл;  
4. **закрыть файл!**

Пример:
```cpp
    #include <iostream> // для работы с текстовыми потоками
    #include <fstream>  // для работы с текстовыми файлами 
    int main(){
        char buff[80];
        std::ifstream file("ourText.txt");  // создаем объект класса и открываем файл ourText.txt
        if (file){  // удостоверимся, что открытие файла прошло корректно
            while(file >> buff){               // считываем слово
                std::cout << buff << "\n";  // выводим слово на экран
            }
        }
        file.close();                       // закрываем файл
        return 0;
    }
```
Для считывания строк используется функция `getline()`:
```cpp
    #include <iostream> // для работы с текстовыми потоками
    #include <fstream>  // для работы с текстовыми файлами
    #include <string>   // для работы со строками
    int main(){
        std::string buff;
        std::ifstream file("ourText.txt");  // создаем объект класса и открываем файл ourText.txt
        if (file){  // удостоверимся, что открытие файла прошло корректно
            while(std::getline(file, buff, ' ')){              // считываем строку
                std::cout << buff << "\n";
            }
        }
        file.close();                       // закрываем файл
        return 0;
    }
```

Пример считывания матрицы из файла:
```cpp
    #include <iostream> // для работы с текстовыми потоками
    #include <fstream>  // для работы с текстовыми файлами
    #include <string>   // для работы со строками
    #include <vector>   // для работы с векторами
    #include <sstream>  // для работы с объектами класса istringstream

    int main(){

        const char separator = '\t'; // символ разделяющий числа в файле (таб)
        std::string token; // переменная для хранения подстроки из потока
        int value; // переменная для хранения числа
    
        std::vector< std::vector<int> > matrix; 

         std::ifstream file("ourMatrix.txt");  // создаем объект класса и открываем файл ourText.txt

         for (std::string line; std::getline(file, line);){ //цикл по строкам в файле
             if ('#' == line[0]){
                 continue;   // c '#' начинаются строки с комментариями
             }
         
             std::istringstream stream(line);  // сохраняем строку в буфер, чтобы безопасно привести ее к нужному типу
             std::vector<int> row;
         
             while(std::getline(stream, token, separator)){ 
                 if (std::istringstream(token) >> value){
                     row.push_back(value);
                 }
             }
             matrix.push_back(row);
         }
         // вывод матрицы на экран
         for (int i = 0; i < matrix.size(); i++){
              for (int j = 0; j < matrix[0].size(); j++){
                  std::cout << std::setw(4) << matrix[i][j];
              }
              std::cout << std::endl;
          }

         file.close();                      // закрываем файл
        return 0;
}

