from math import (
    sin,
    cos,
    tan,
    radians
)
from nodes import *
from values import Number

class Interpreter:
    def visit(self, node):
        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name)
        return method(node)

    def visit_NumberNode(self, node):
        return Number(node.value)

    def visit_AddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)
    
    def visit_SubtractNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)
    
    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)
    
    def visit_DivideNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except Exception:
            raise Exception("Runtime math error")

    def visit_ExponentNode(self, node):
        return Number(pow(self.visit(node.node_a).value, self.visit(node.node_b).value))

    def visit_SinNode(self, node):
        return Number(sin(radians(node.node.value)))

    def visit_CosNode(self, node):
        return Number(cos(radians(node.node.value)))

    def visit_TanNode(self, node):
        return Number(tan(radians(node.node.value)))

    def visit_CotNode(self, node):
        return Number(cos(radians(node.node.value))/sin(radians(node.node.value)))

    def visit_SecNode(self, node):
        return Number(1/cos(radians(node.node.value)))

    def visit_CscNode(self, node):
        return Number(1/sin(radians(node.node.value)))

    def visit_PlusNode(self, node):
        return self.visit(node.node)
    
    def visit_MinusNode(self, node):
        return Number(-self.visit(node.node).value)
