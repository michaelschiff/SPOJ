import sys

def next_matching_index(expr):
    depth = 1
    for (i, char) in enumerate(expr):
        if char == '(': depth += 1
        if char == ')': depth -= 1
        if depth == 0: return i


def parse(expr):
    expr = expr.strip()
    if len(expr) > 1:
        if expr[0] == '(':
            closing = next_matching_index(expr[1:]) + 1
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

def to_rpn(expr, so_far):
    (left, op, right) = parse(expr)
    if left:
        if len(left) == 1:
            so_far += left
        else:
            so_far = to_rpn(left, so_far)
        
    if right:
        if right and len(right) == 1:
            so_far += right
        else:
            so_far = to_rpn(right, so_far)

    if op:
        so_far += op

    return so_far


if __name__ == "__main__":
    num_cases = int(sys.stdin.readline())
    for case in range(num_cases):
        print(to_rpn(sys.stdin.readline(), ""))




