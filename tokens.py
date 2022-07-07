from dataclasses import dataclass
from enum import Enum

class TokenType(Enum):
    NUMBER       = 0
    PLUS         = 1
    MINUS        = 2
    MULTIPLY     = 3
    DIVIDE       = 4
    LPAREN       = 5
    RPAREN       = 6
    EXPONENT     = 7
    SIN_TRIG     = 8
    COS_TRIG     = 9
    TAN_TRIG     = 10
    COT_TRIG     = 11
    SEC_TRIG     = 12
    CSC_TRIG     = 13


@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self) -> str:
        return self.type.name + (f":{self.value}" if self.value != None else "")
