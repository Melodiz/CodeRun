def check_brackets(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if stack == [] or bracket_map[char] != stack.pop():
                return False
    return stack == []

def main():
    s = input().strip()
    if check_brackets(s):
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()