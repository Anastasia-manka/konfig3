#дз3
import re
import sys
import yaml
import operator

class ConfigParser:
    def __init__(self):
        self.variables = {}
        self.ops = {
            '+': operator.add,
            '-': operator.sub,
        }

    def parse(self, input_text):
        lines = input_text.splitlines()
        in_multiline_comment = False
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if not line:
                continue
            if line.startswith("'"):  # Однострочный комментарий
                continue
            if line.startswith("--[["):  # Начало многострочного комментария
                in_multiline_comment = True
                continue
            if line.startswith("]]"):  # Конец многострочного комментария
                in_multiline_comment = False
                continue
            if in_multiline_comment:
                continue
            if line.startswith("def "):
                self.handle_definition(line, line_num)
            elif line.startswith("|"):
                self.handle_expression(line, line_num)
            else:
                self.handle_assignment(line, line_num)

    def handle_definition(self, line, line_num):
        match = re.match(r"def (\w+) = (.+)", line)
        if match:
            name, value = match.groups()
            try:
                self.variables[name] = self.parse_value(value)
            except ValueError as e:
                print(f"Ошибка на строке {line_num}: {e}")
        else:
            print(f"Синтаксическая ошибка на строке {line_num}: {line}")

    def handle_expression(self, line, line_num):
        try:
            expression = line[1:].strip()
            result = self.evaluate_expression(expression)
            #  В данном случае, просто выводим результат
            print(f"Вычисление выражения на строке {line_num}: {result}")
        except (ValueError, KeyError, TypeError) as e:
            print(f"Ошибка на строке {line_num}: {e}")

    def handle_assignment(self, line, line_num):
        match = re.match(r"(\w+) = (.+)", line)
        if match:
            name, value = match.groups()
            try:
                self.variables[name] = self.parse_value(value)
            except ValueError as e:
                print(f"Ошибка на строке {line_num}: {e}")
        else:
            print(f"Синтаксическая ошибка на строке {line_num}: {line}")

    def parse_value(self, value):
        if value.startswith("q(") and value.endswith(")"):
            return value[2:-1]  # Строка
        elif value.startswith("{") and value.endswith("}"):
            return self.parse_array(value[1:-1])
        elif value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
            return int(value)  # Число
        elif value in self.variables:
            return self.variables[value]  # Переменная
        else:
            raise ValueError(f"Неизвестное значение: {value}")

    def parse_array(self, array_str):
        items = [item.strip() for item in array_str.split(",")]
        return [self.parse_value(item) for item in items]

    def evaluate_expression(self, expression):
        tokens = re.findall(r"(\w+)|(\+)|(-)", expression)
        stack = []
        for token_pair in tokens:
            token = next((t for t in token_pair if t), None)
            if token is None: continue
            if token in self.ops:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.ops[token](op1, op2))
            elif token in self.variables:
                stack.append(self.variables[token])
            else:
                try:
                    stack.append(int(token))
                except ValueError:
                    raise ValueError(f"Неизвестный токен: {token}")
        if len(stack) != 1:
            raise ValueError("Некорректное выражение")
        return stack[0]

def main():
    parser = ConfigParser()
    print("Введите конфигурацию (введите 'end' для завершения):")
    input_lines = []
    while True:
        line = input()
        if line.lower() == 'end':
            break
        input_lines.append(line)
    input_text = '\n'.join(input_lines)
    parser.parse(input_text)
    print(yaml.dump(parser.variables, allow_unicode=True, default_flow_style=False))

if __name__ == "__main__":
    main()