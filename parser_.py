from tokens import TokenType
from nodes import *


class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None
        
    def parse(self):
        if self.current_token == None:
            return None

        result = self.expr()

        if self.current_token != None:
            raise Exception("Invalid syntax")

        return result

    def expr(self):
        result = self.term()

        while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.term())
            elif self.current_token.type == TokenType.MINUS:
                self.advance()
                result = SubtractNode(result, self.term())
        
        return result

    def term(self):
        result = self.intermediate_factor()

        while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            if self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result, self.intermediate_factor())
            elif self.current_token.type == TokenType.DIVIDE:
                self.advance()
                result = DivideNode(result, self.intermediate_factor())

        return result

    def intermediate_factor(self):
        result = self.factor()

        if self.current_token != None and self.current_token.type == TokenType.EXPONENT:
            self.advance()
            result = ExponentNode(result, self.factor())

        return result

    def factor(self):
        token = self.current_token

        if token.type == TokenType.LPAREN:
            self.advance()
            result = self.expr()
            if self.current_token.type != TokenType.RPAREN:
                raise Exception("Invalid syntax")

            self.advance()
            return result
        elif token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)
        elif token.type == TokenType.PLUS:
            self.advance()
            return PlusNode(self.factor())
        elif token.type == TokenType.MINUS:
            self.advance()
            return MinusNode(self.factor())
        elif token.type == TokenType.SIN_TRIG:
            self.advance()
            return SinNode(token.value)
        elif token.type == TokenType.COS_TRIG:
            self.advance()
            return CosNode(token.value)
        elif token.type == TokenType.TAN_TRIG:
            self.advance()
            return TanNode(token.value)
        elif token.type == TokenType.COT_TRIG:
            self.advance()
            return CotNode(token.value)
        elif token.type == TokenType.SEC_TRIG:
            self.advance()
            return SecNode(token.value)
        elif token.type == TokenType.CSC_TRIG:
            self.advance()
            return CscNode(token.value) 
        raise Exception("Invalid syntax")
