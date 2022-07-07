import unittest
from tokens import Token, TokenType
from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter
from nodes import *
from values import Number

class TestLexer(unittest.TestCase):
    def test_empty(self):
        tokens = list(Lexer("").generate_tokens())
        self.assertEqual(tokens, [])
    
    def test_spaces(self):
        tokens = list(Lexer("  \t   \n \t\t   \n\n\n  ").generate_tokens())
        self.assertEqual(tokens, [])
    
    def test_numbers(self):
        tokens = list(Lexer("123 123.321 12. .21 . 00").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 123.0),
            Token(TokenType.NUMBER, 123.321),
            Token(TokenType.NUMBER, 12.0),
            Token(TokenType.NUMBER, 0.21),
            Token(TokenType.NUMBER, 0.0),
            Token(TokenType.NUMBER, 0.0),
        ])
    
    def test_operators(self):
        tokens = list(Lexer("/*-+^").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.DIVIDE),
            Token(TokenType.MULTIPLY),
            Token(TokenType.MINUS),
            Token(TokenType.PLUS),
            Token(TokenType.EXPONENT),
        ])

    def test_sin(self):
        tokens = list(Lexer("sin(22)").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.SIN_TRIG, Token(TokenType.NUMBER, 22.0))
        ])

    def test_cos(self):
        tokens = list(Lexer("cos(22)").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.COS_TRIG, Token(TokenType.NUMBER, 22.0))
        ])

    def test_tan(self):
        tokens = list(Lexer("tan(22)").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.TAN_TRIG, Token(TokenType.NUMBER, 22.0))
        ])

    def test_cot(self):
        tokens = list(Lexer("cot(22)").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.COT_TRIG, Token(TokenType.NUMBER, 22.0))
        ])

    def test_sec(self):
        tokens = list(Lexer("sec(22)").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.SEC_TRIG, Token(TokenType.NUMBER, 22.0))
        ])

    def test_csc(self):
        tokens = list(Lexer("csc(22)").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.CSC_TRIG, Token(TokenType.NUMBER, 22.0))
        ])

    def test_parenthesis(self):
        tokens = list(Lexer("()").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.LPAREN),
            Token(TokenType.RPAREN),
        ])

    def test_operand(self):
        tokens = list(Lexer("8 * ( 23 - 4 ^ 2 ) / 2 + 38 - ( 12 * 4 )").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 8.0),
            Token(TokenType.MULTIPLY),
            Token(TokenType.LPAREN),
            Token(TokenType.NUMBER, 23.0),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 4.0),
            Token(TokenType.EXPONENT),
            Token(TokenType.NUMBER, 2.0),
            Token(TokenType.RPAREN),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 2),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 38),
            Token(TokenType.MINUS),
            Token(TokenType.LPAREN),
            Token(TokenType.NUMBER, 12),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 4),
            Token(TokenType.RPAREN),
        ])


class TestParser(unittest.TestCase):
    def test_empty(self):
        tokens = []
        nodes = Parser(tokens).parse()
        self.assertEqual(nodes, None)
    
    def test_number(self):
        tokens = [
            Token(TokenType.NUMBER, 12.3)
        ]
        nodes = Parser(tokens).parse()
        self.assertEqual(nodes, NumberNode(12.3))
    
    def test_add(self):
        tokens = [
            Token(TokenType.NUMBER, 12.4),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 12.4)
        ]
        nodes = Parser(tokens).parse()
        self.assertEqual(nodes, AddNode(NumberNode(12.4), NumberNode(12.4)))
    
    def test_sub(self):
        tokens = [
            Token(TokenType.NUMBER, 12.4),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 12.4)
        ]
        nodes = Parser(tokens).parse()
        self.assertEqual(nodes, SubtractNode(NumberNode(12.4), NumberNode(12.4)))
    
    def test_mul(self):
        tokens = [
            Token(TokenType.NUMBER, 12.4),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 12.4)
        ]
        nodes = Parser(tokens).parse()
        self.assertEqual(nodes, MultiplyNode(NumberNode(12.4), NumberNode(12.4)))

    def test_div(self):
        tokens = [
            Token(TokenType.NUMBER, 12.4),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 12.4)
        ]
        nodes = Parser(tokens).parse()
        self.assertEqual(nodes, DivideNode(NumberNode(12.4), NumberNode(12.4)))

    def test_exponent(self):
        tokens = [
            Token(TokenType.NUMBER, 3),
            Token(TokenType.EXPONENT),
            Token(TokenType.NUMBER, 4)
        ]
        nodes = Parser(tokens).parse()
        self.assertEqual(nodes, ExponentNode(NumberNode(3), NumberNode(4)))

    def test_sin(self):
        tokens = [
            Token(TokenType.SIN_TRIG, Token(TokenType.NUMBER, 22.0))
        ]
        nodes = Parser(tokens).parse()
        self.assertEqual(nodes, SinNode(Token(TokenType.NUMBER, 22.0)))

    def test_cos(self):
        tokens = [
            Token(TokenType.COS_TRIG, Token(TokenType.NUMBER, 22.0))
        ]
        nodes = Parser(tokens).parse()
        self.assertEqual(nodes, CosNode(Token(TokenType.NUMBER, 22.0)))

    def test_tan(self):
        tokens = [
            Token(TokenType.TAN_TRIG, Token(TokenType.NUMBER, 22.0))
        ]
        nodes = Parser(tokens).parse()
        self.assertEqual(nodes, TanNode(Token(TokenType.NUMBER, 22.0)))

    def test_cot(self):
        tokens = [
            Token(TokenType.COT_TRIG, Token(TokenType.NUMBER, 22.0))
        ]
        nodes = Parser(tokens).parse()
        self.assertEqual(nodes, CotNode(Token(TokenType.NUMBER, 22.0)))

    def test_sec(self):
        tokens = [
            Token(TokenType.SEC_TRIG, Token(TokenType.NUMBER, 22.0))
        ]
        nodes = Parser(tokens).parse()
        self.assertEqual(nodes, SecNode(Token(TokenType.NUMBER, 22.0)))

    def test_csc(self):
        tokens = [
            Token(TokenType.CSC_TRIG, Token(TokenType.NUMBER, 22.0))
        ]
        nodes = Parser(tokens).parse()
        self.assertEqual(nodes, CscNode(Token(TokenType.NUMBER, 22.0)))

    def test_operation(self):
        # operation = 8 * ( 23 - 4 ^ 2 ) / 2 + 38
        tokens = [
            Token(TokenType.NUMBER, 8),
            Token(TokenType.MULTIPLY),
            Token(TokenType.LPAREN),
            Token(TokenType.NUMBER, 23),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 4),
            Token(TokenType.EXPONENT),
            Token(TokenType.NUMBER, 2),
            Token(TokenType.RPAREN),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 2),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 38),
        ]
        nodes = Parser(tokens).parse()
        self.assertEqual(nodes, AddNode(
            DivideNode(
                MultiplyNode(
                    NumberNode(8),
                    SubtractNode(
                        NumberNode(23),
                        ExponentNode(
                            NumberNode(4),
                            NumberNode(2)
                        )
                    )
                ),
                NumberNode(2)
            ),
            NumberNode(38)
        ))


class TestInterpreter(unittest.TestCase):
    def test_number(self):
        result = Interpreter().visit(NumberNode(34.4))
        self.assertEqual(result, Number(34.4))
    
    def test_operations(self):
        result = Interpreter().visit(AddNode(NumberNode(21), NumberNode(11)))
        self.assertEqual(result, Number(32))

        result = Interpreter().visit(SubtractNode(NumberNode(21), NumberNode(11)))
        self.assertEqual(result, Number(10))

        result = Interpreter().visit(MultiplyNode(NumberNode(21), NumberNode(11)))
        self.assertEqual(result, Number(231))

        result = Interpreter().visit(DivideNode(NumberNode(100), NumberNode(20)))
        self.assertEqual(result, Number(5.0))

        with self.assertRaises(Exception):
            Interpreter().visit(DivideNode(NumberNode(21), NumberNode(0)))

    def test_trig_functions(self):
        result = Interpreter().visit(SinNode(NumberNode(22)))
        self.assertAlmostEqual(result.value, 0.37460659)

        result = Interpreter().visit(CosNode(NumberNode(22)))
        self.assertAlmostEqual(result.value, 0.92718385)

        result = Interpreter().visit(TanNode(NumberNode(22)))
        self.assertAlmostEqual(result.value, 0.40402622)

        result = Interpreter().visit(CotNode(NumberNode(22)))
        self.assertAlmostEqual(result.value, 2.47508685)

        result = Interpreter().visit(SecNode(NumberNode(22)))
        self.assertAlmostEqual(result.value, 1.07853474)

        result = Interpreter().visit(CscNode(NumberNode(22)))
        self.assertAlmostEqual(result.value, 2.66946716)

    def test_expression(self):
        #  8 * ( 23 - 4 ^ 2 ) / 2 + 38
        tree = AddNode(
            DivideNode(
                MultiplyNode(
                    NumberNode(8),
                    SubtractNode(
                        NumberNode(23),
                        ExponentNode(
                            NumberNode(4),
                            NumberNode(2)
                        )
                    )
                ),
                NumberNode(2)
            ),
            NumberNode(38)
        )
        result = Interpreter().visit(tree)
        self.assertEqual(result, Number(66.0))
