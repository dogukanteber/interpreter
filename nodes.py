from dataclasses import dataclass

@dataclass
class NumberNode:
    value: float

    def __repr__(self):
        return f"{self.value}"


@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} + {self.node_b})"


@dataclass
class SubtractNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} - {self.node_b})"


@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} * {self.node_b})"


@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} / {self.node_b})"


@dataclass
class ExponentNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a} / {self.node_b})"


@dataclass
class SinNode:
    node: any

    def __repr__(self):
        return f"{self.node}"


@dataclass
class CosNode:
    node: any

    def __repr__(self):
        return f"{self.node}"


@dataclass
class TanNode:
    node: any

    def __repr__(self):
        return f"{self.node}"


@dataclass
class CotNode:
    node: any

    def __repr__(self):
        return f"{self.node}"


@dataclass
class SecNode:
    node: any

    def __repr__(self):
        return f"{self.node}"

@dataclass
class CscNode:
    node: any

    def __repr__(self):
        return f"{self.node}"


@dataclass
class PlusNode:
    node: any

    def __repr__(self):
        return f"(+{self.node})"


@dataclass
class MinusNode:
    node: any

    def __repr__(self):
        return f"(-{self.node})"
