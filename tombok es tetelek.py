import ast
import operator
import sys

#!/usr/bin/env python3
"""
Simple safe calculator REPL.

Supports: + - * / // % ** unary +/-, parentheses and the special variable `ans`.
Type "quit" or "exit" to leave, "help" for usage and "history" to see past calculations.
"""


ALLOWED_BINOPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

ALLOWED_UNARYOPS = {
    ast.UAdd: lambda x: +x,
    ast.USub: lambda x: -x,
}


class EvalError(Exception):
    pass


def safe_eval(expr: str, names: dict):
    """
    Evaluate a numeric expression safely using ast.
    Allowed: numbers, parentheses, binary ops (+ - * / // % **),
    unary +/-, and the name 'ans' (if provided in names).
    """
    try:
        node = ast.parse(expr, mode="eval")
    except SyntaxError as e:
        raise EvalError("syntax error") from e

    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Constant):  # Python 3.8+
            if isinstance(node.value, (int, float)):
                return node.value
            raise EvalError("only numeric constants allowed")
        if isinstance(node, ast.Num):  # older versions
            return node.n
        if isinstance(node, ast.BinOp):
            left = _eval(node.left)
            right = _eval(node.right)
            op_type = type(node.op)
            if op_type in ALLOWED_BINOPS:
                try:
                    return ALLOWED_BINOPS[op_type](left, right)
                except ZeroDivisionError as e:
                    raise EvalError("division by zero") from e
            raise EvalError(f"operator {op_type} not allowed")
        if isinstance(node, ast.UnaryOp):
            operand = _eval(node.operand)
            op_type = type(node.op)
            if op_type in ALLOWED_UNARYOPS:
                return ALLOWED_UNARYOPS[op_type](operand)
            raise EvalError("unary operator not allowed")
        if isinstance(node, ast.Name):
            if node.id in names:
                val = names[node.id]
                if isinstance(val, (int, float)):
                    return val
            raise EvalError(f"unknown name: {node.id}")
        # disallow everything else (calls, attributes, subscripts, etc.)
        raise EvalError(f"disallowed expression: {type(node).__name__}")

    return _eval(node)


def repl():
    print("Simple calculator. Type 'help' for instructions.")
    ans = 0
    history = []
    while True:
        try:
            s = input("calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not s:
            continue
        if s.lower() in ("quit", "exit"):
            break
        if s.lower() == "help":
            print("Enter arithmetic expressions using + - * / // % ** and parentheses.")
            print("You can use 'ans' to refer to the previous result.")
            print("Commands: help, history, quit, exit")
            continue
        if s.lower() == "history":
            if not history:
                print("(no history)")
            else:
                for i, (expr, res) in enumerate(history, 1):
                    print(f"{i}: {expr} = {res}")
            continue

        try:
            result = safe_eval(s, {"ans": ans})
        except EvalError as e:
            print("Error:", e)
            continue
        except Exception:
            print("Error: evaluation failed")
            continue

        # Normalize int vs float display
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        print(result)
        history.append((s, result))
        ans = result


if __name__ == "__main__":
    repl()