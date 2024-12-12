# Вариант 14 практики 2
## Постановка задачи
Разработать инструмент командной строки для учебного конфигурационного языка, который преобразует текст из входного формата в выходной. Входной текст принимается из стандартного ввода, а выходной текст на языке YAML выводится в стандартный вывод. Инструмент должен поддерживать следующие конструкции языка:

Однострочные комментарии: начинаются с символа '.

Многострочные комментарии: начинаются с --[[ и заканчиваются ]].

Массивы: заключаются в фигурные скобки {} и содержат список значений, разделенных запятыми.

Имена: состоят из букв в диапазоне [a-z]+.

Значения: могут быть числами, строками или массивами.

Строки: заключаются в q() (например, q(Это строка)).

Объявление констант: используется ключевое слово def, например, def имя = значение.

Константные выражения: вычисляются на этапе трансляции в постфиксной форме, например, |имя 1 +|.

Операции и функции: поддерживаются операции сложения, вычитания, а также функции print() и chr().

Инструмент должен выявлять синтаксические ошибки и выдавать соответствующие сообщения. Все конструкции языка должны быть покрыты тестами, включая примеры из разных предметных областей.

## Описание проекта
Проект представляет собой консольное приложение, написанное на Python, которое читает текст на учебном конфигурационном языке из стандартного ввода, обрабатывает его и преобразует в формат YAML, который выводится в стандартный вывод.

Основные функции проекта:

### Парсинг входного текста:

Обработка однострочных и многострочных комментариев.

Разбор массивов, строк, чисел и имен.

Объявление и использование констант.

Вычисление константных выражений.

### Преобразование в YAML:

Результаты обработки текста преобразуются в формат YAML и выводятся в консоль.

### Обработка ошибок:

Выявление и вывод сообщений о синтаксических ошибках.

### Тестирование:

Покрытие всех конструкций языка тестами.

Примеры из разных предметных областей.

## Описание классов
Проект состоит из одного основного класса ConfigParser, который отвечает за обработку входного текста и преобразование его в YAML.

### Класс ConfigParser
## 
### Методы:

__init__(): Инициализация объекта, создание словаря для хранения переменных.

parse(input_text): Основной метод для обработки входного текста. Разделяет текст на строки и обрабатывает каждую строку в зависимости от её типа.

handle_definition(line): Обработка объявления константы с помощью ключевого слова def.

handle_expression(line): Обработка константных выражений в постфиксной форме.

handle_assignment(line): Обработка присваивания значений переменным.

parse_value(value): Разбор значений (числа, строки, массивы, переменные).

parse_array(array_str): Разбор массивов, содержащихся в фигурных скобках.

### Атрибуты:

variables: Словарь для хранения объявленных переменных и их значений.

## Описание тестирования
Тестирование проекта включает покрытие всех конструкций языка и проверку корректной работы инструмента. Для тестирования используется модуль unittest или pytest.

Примеры тестов:

Однострочные комментарии:

Ввод: ' Это комментарий.

Ожидаемый результат: комментарий игнорируется, вывод пустой.

Многострочные комментарии:

Ввод: --[[ Это комментарий ]].

Ожидаемый результат: комментарий игнорируется, вывод пустой.

Массивы:

Ввод: arr = {1, 2, 3}.

Ожидаемый результат: arr: [1, 2, 3].

Строки:

Ввод: str = q(Пример строки).

Ожидаемый результат: str: Пример строки.

Объявление констант:

Ввод: def x = 10.

Ожидаемый результат: x: 10.

Константные выражения:

Ввод: |x 5 +|.

Ожидаемый результат: вычисление выражения и вывод результата.

Синтаксические ошибки:

Ввод: x = неизвестное_значение.

Ожидаемый результат: сообщение об ошибке.

![image](https://github.com/user-attachments/assets/509cbc7d-3d2d-40a4-aca3-c516c5c2ac3d)

![image](https://github.com/user-attachments/assets/7240e83d-b33e-4244-88d2-a5d02861640c)

![image](https://github.com/user-attachments/assets/2f3b0853-1bc4-476e-b7c9-f8512434aa57)

![image](https://github.com/user-attachments/assets/5597f712-34f2-4086-8d48-1488daa169ff)

