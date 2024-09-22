def check_parentheses(expression):
    stack = []
    parens = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in parens.values():
            stack.append(char)
        elif char in parens:
            if not stack or stack.pop() != parens[char]:
                return "no"

    if not stack:
        print("The stack is empty.")
    return "yes" if not stack else "no"

if __name__ == "__main__":
    import sys

    expression = sys.argv[1]
    print(check_parentheses(expression))
