#дз3
import re
import sys
import yaml

class ConfigParser:
    def __init__(self):
        self.variables = {}
    
    def parse(self, input_text):
        lines = input_text.splitlines()
        for line in lines:
            line = line.strip()
            if not line or line.startswith("'"):  # Однострочный комментарий
                continue
            elif line.startswith("--[["):  # Начало многострочного комментария
                continue
            elif line.startswith("]]"):  # Конец многострочного комментария
                continue
            elif line.startswith("def "):
                self.handle_definition(line)
            elif line.startswith("|"):
                self.handle_expression(line)
            else:
                self.handle_assignment(line)

    def handle_definition(self, line):
        match = re.match(r"def (\w+) = (.+)", line)
        if match:
            name, value = match.groups()
            self.variables[name] = self.parse_value(value)
        else:
            print(f"Синтаксическая ошибка в строке: {line}")

    def handle_expression(self, line):
        expression = line[1:].strip()
        # Здесь можно добавить логику для обработки выражений
        print(f"Вычисление выражения: {expression}")

    def handle_assignment(self, line):
        match = re.match(r"(\w+) = (.+)", line)
        if match:
            name, value = match.groups()
            self.variables[name] = self.parse_value(value)
        else:
            print(f"Синтаксическая ошибка в строке: {line}")

    def parse_value(self, value):
        if value.startswith("q(") and value.endswith(")"):
            return value[2:-1]  # Строка
        elif value.startswith("{") and value.endswith("}"):
            return self.parse_array(value[1:-1])
        elif value.isdigit():
            return int(value)  # Число
        elif value in self.variables:
            return self.variables[value]  # Переменная
        else:
            print(f"Неизвестное значение: {value}")
            return None

    def parse_array(self, array_str):
        items = [item.strip() for item in array_str.split(",")]
        return [self.parse_value(item) for item in items]

def main():
    input_text = sys.stdin.read()
    parser = ConfigParser()
    parser.parse(input_text)
    # Преобразуем в YAML и выводим
    print(yaml.dump(parser.variables, allow_unicode=True))

if __name__ == "__main__":
    main()