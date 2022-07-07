from tokens import Token, TokenType
from string import ascii_letters as LETTERS
from string import digits, whitespace

TRIGONOMETRIC_FUNCTIONS = ("sin", "cos", "tan", "cot", "sec", "csc")

class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char != None:
            if self.current_char in whitespace:
                self.advance()
            elif self.current_char in digits or self.current_char == '.':
                yield self.generate_number()
            elif self.current_char in LETTERS:
                yield self.generate_trig_function()
            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RPAREN)
            elif self.current_char == '^':
                self.advance()
                yield Token(TokenType.EXPONENT)
            else:
                raise Exception(f"Illegal character: '{self.current_char}'")

    def generate_trig_function(self):
        func_str = self.current_char
        self.advance()

        while self.current_char != None and self.current_char in LETTERS:
            func_str += self.current_char
            self.advance()
        
        if func_str not in TRIGONOMETRIC_FUNCTIONS:
            raise Exception(f"Illegal function: {func_str}")

        if self.current_char == '(':
            self.advance()
            number_str = self.generate_number()
            if self.current_char == ')':
                self.advance()
                if func_str == "sin":
                    return Token(TokenType.SIN_TRIG, number_str)
                elif func_str == "cos":
                    return Token(TokenType.COS_TRIG, number_str)
                elif func_str == "tan":
                    return Token(TokenType.TAN_TRIG, number_str)
                elif func_str == "cot":
                    return Token(TokenType.COT_TRIG, number_str)
                elif func_str == "sec":
                    return Token(TokenType.SEC_TRIG, number_str)
                elif func_str == "csc":
                    return Token(TokenType.CSC_TRIG, number_str)

        raise Exception("Invalid syntax")

    def generate_number(self):
        decimal_point_count = 0
        number_str = self.current_char
        self.advance()

        while self.current_char != None and (self.current_char == '.' or self.current_char in digits):
            if self.current_char == '.':
                decimal_point_count += 1
            if decimal_point_count > 1:
                break

            number_str += self.current_char
            self.advance()
        
        if number_str.startswith('.'):
            number_str = '0' + number_str

        if number_str.endswith('.'):
            number_str = number_str + '0'
        
        return Token(TokenType.NUMBER, float(number_str))
