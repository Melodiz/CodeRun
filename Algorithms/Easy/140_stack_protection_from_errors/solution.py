from sys import stdin

def main():
    stack = []
    for line in stdin.readlines():
        if line.strip() == "exit": print("bye"); return
        elif line.strip() == "pop": print(stack.pop()) if stack else print("error")
        elif line.strip() == "back": print(stack[-1]) if stack else print("error")
        elif line.strip() == "size": print(len(stack))
        elif line.strip() == "clear": stack = []; print("ok")
        else:
            command, value = line.strip().split()
            if command == "push": stack.append(int(value)); print("ok")
    

if __name__ == "__main__":
    main()