import sys

def parse(expr):
    expr = expr.strip()
    if len(expr) > 1:
        if expr[0] == '(':
            closing = expr.rfind(')')
            left = expr[1:closing]
            if closing + 1 == len(expr):
                return (left, None, None)
            op = expr[closing+1]
            right = expr[closing+2:]
            return (left, op, right)
        else:
            left = expr[0]
            op = expr[1]
            right = expr[2:]
            return (left, op, right)
    else:
        return (expr, None, None)

def to_rpn(expr):
    print parse(expr)

if __name__ == "__main__":
    num_cases = int(sys.stdin.readline())
    for case in range(num_cases):
        to_rpn(sys.stdin.readline())




