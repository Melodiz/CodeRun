from sys import stdin
def main():
    deque = []
    for line in stdin.readlines():
        if line.strip() == "exit":
            print("bye"); return
        elif line.strip() == "pop_front":
            if not deque: print("error")
            else: print(deque.pop(0))
        elif line.strip() == "pop_back":
            if not deque: print("error")
            else: print(deque.pop())
        elif line.strip() == "size":
            print(len(deque))
        elif line.strip() == "clear":
            deque = []; print("ok")
        elif line.strip() == "front":
            if not deque: print("error")
            else: print(deque[0])
        elif line.strip() == "back":
            if not deque: print("error")
            else: print(deque[-1])
        else:
            command, value = line.strip().split()
            if command == "push_front":
                deque.insert(0, int(value))
                print("ok")
            else:
                deque.append(int(value))
                print("ok")
        
if __name__ == "__main__":
    main()