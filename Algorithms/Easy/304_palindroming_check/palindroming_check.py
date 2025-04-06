def main():
    s = input()
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalpha(): 
            left += 1; continue
        if not s[right].isalpha():
            right -= 1; continue
        if s[left].lower() != s[right].lower():
            return "It is not a palindrome"
        left += 1
        right -= 1
    return "It is a palindrome"

if __name__ == "__main__":
    print(main())