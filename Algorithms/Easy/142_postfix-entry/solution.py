def Reverse_Polish_notation(char_stack):
    stack = []
    for token in char_stack:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
    return stack[0]

def main():
    chars = input().strip().split()
    print(Reverse_Polish_notation(chars))

if __name__ == "__main__":
    main()