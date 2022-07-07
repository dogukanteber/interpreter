import readline  # imported for input() method to move text cursor

from interpreter import Interpreter
from lexer import Lexer
from parser_ import Parser

while True:
    try:
        text = input("math > ")
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if not tree: continue
        interpreter = Interpreter()
        res = interpreter.visit(tree)
        print(res)
    except Exception as e:
        print(e)