import re

def tokenize(expression):
    """
    Splits the input expression into tokens.
    Handles numbers, operators, and parentheses.
    """
    token_pattern = r'\d+|\+|\*|\^|\(|\)'
    tokens = re.findall(token_pattern, expression)
    return tokens

def evaluate_tokens(tokens):
    """
    Evaluates the tokenized expression following the PEMDAS rules.
    Handles parentheses, exponentiation, multiplication,
    division, addition, and subtraction.
    """
    # Handle parentheses first
    while '(' in tokens:
        close_idx = tokens.index(')')
        open_idx = max(i for i, token in enumerate(tokens[:close_idx]) if token == '(')
        result = evaluate_simple(tokens[open_idx + 1:close_idx])
        tokens = tokens[:open_idx] + [str(result)] + tokens[close_idx + 1:]

    return evaluate_simple(tokens)

def evaluate_simple(tokens):
    """
    Evaluates a tokenized expression without parentheses.
    Handles PEMDAS (Exponentiation first, then Multiplication/Division, and Addition/Subtraction).
    """
    while '^' in tokens:
        idx = tokens.index('^')
        base = float(tokens[idx - 1])
        exponent = float(tokens[idx + 1])
        result = base ** exponent
        tokens = tokens[:idx - 1] + [str(result)] + tokens[idx + 2:]

    i = 0
    while i < len(tokens):
        if tokens[i] == '*':
            left = float(tokens[i - 1])
            right = float(tokens[i + 1])
            result = left * right
            tokens = tokens[:i - 1] + [str(result)] + tokens[i + 2:]
        else:
            i += 1

    i = 0
    while i < len(tokens):
        if tokens[i] == '+':
            left = float(tokens[i - 1])
            right = float(tokens[i + 1])
            result = left + right
            tokens = tokens[:i - 1] + [str(result)] + tokens[i + 2:]
        else:
            i += 1

    return float(tokens[0])

# Main program
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        input_expression = sys.argv[1]

        tokens = tokenize(input_expression)

        result = evaluate_tokens(tokens)

        if result.is_integer():
            print(int(result))
        else:
            print(result)
    else:
        print("Usage: python calculator.py '<expression>'")
