# excellent problem, tests your knowledge on stacks and very fun

def evalRPN(tokens) -> int:
    stack = []
    for token in tokens:
        b = int(stack.pop())
        a = int(stack.pop())
        if token == "+":
            stack.append(a+b)
        elif token == "-":
            stack.append(a-b)
        elif token == "*":
            stack.append(a*b)
        elif token == "/":
            stack.append(a/b)  # no need to cast to int because it will be cast when being popped from the stack
        else:
            stack.append(token)

    return int(stack[0])


print(evalRPN(["18"]))
