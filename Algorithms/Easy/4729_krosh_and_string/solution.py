# Solution for https://coderun.yandex.ru/problem/krosh-and-string
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    n = int(input()) 
    s = input()      

    stack = []       

    for char in s:   
        if stack and stack[-1] == char:
            stack.pop() 
        else:
            stack.append(char) 
    return 1 if not stack else 0

if __name__ == "__main__":
    print(main())