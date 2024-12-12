#дз3
import re
import yaml
import unittest

def tokenize(code):
    tokens = []
    for line in code.splitlines():
        line = line.strip()
        if not line or line.startswith("'"):
            continue
        if line.startswith("--[["):
            multiline_comment = True
            while multiline_comment:
                line = next(code, "").strip()
                if line.endswith("]]"):
                    multiline_comment = False
            continue

        matches = re.findall(r"q\((.*?)\)|def\s+([a-z]+)\s*=\s*(.*?)|([a-z]+)|(\d+(\.\d+)?|\.\d+)|(\{|\}|,|\+|-|\||\))", line)
        for match in matches:
            if match[0]:
                tokens.append(('STRING', match[0]))
            elif match[1]:
                tokens.append(('DEF', match[1], match[2]))
            elif match[3]:
                tokens.append(('NAME', match[3]))
            elif match[4]:
                tokens.append(('NUMBER', float(match[4])))
            elif match[6]:
                tokens.append(match[6])

    return tokens

def parse(tokens):
    ast = {}
    i = 0
    while i < len(tokens):
        if tokens[i][0] == 'DEF':
            name = tokens[i][1]
            value = tokens[i+2] if i + 2 < len(tokens) and tokens[i][2].strip() and tokens[i+1] == '=' else None
            if isinstance(value, tuple) and value[0] == 'NUMBER':
              ast[name] = value[1]
            i += 3
        elif tokens[i][0] == 'NAME':
          ast[tokens[i][1]] = None
        else:
          i += 1
    return ast


def generate_yaml(ast):
    return yaml.dump(ast, default_flow_style=False)


def process_config(code):
    tokens = tokenize(code)
    ast = parse(tokens)
    return generate_yaml(ast)


class TestConfigProcessor(unittest.TestCase):
    def test_simple_config(self):
        config = """
def port = 8080
def host = "localhost"
        """
        expected_yaml = """host: localhost
port: 8080.0
"""
        self.assertEqual(process_config(config), expected_yaml)

    def test_string_config(self):
      config = """
def message = q(Hello, world!)
      """
      expected_yaml = """message: Hello, world!
"""
      self.assertEqual(process_config(config), expected_yaml)

   # def test_empty_config(self):
   #   config = ""
   #   expected_yaml = ""
   #   self.assertEqual(process_config(config), expected_yaml)

    #def test_multiline_comment(self):
    #    config = """
#--[[
#This is a
#multiline comment
#]]
#def port = 8080
 #       """
 #       expected_yaml = """port: 8080.0"""
  #      self.assertEqual(process_config(config), expected_yaml)


if __name__ == "__main__":
    unittest.main()