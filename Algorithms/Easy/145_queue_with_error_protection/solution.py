import sys
def main():
    queue = []
    for line in sys.stdin.readlines():
        if line.strip() == "exit":
            print("bye"); return
        elif line.strip() == "pop":
            if not queue: print("error")
            else: print(queue.pop(0))
        elif line.strip() == "front":
            if not queue: print("error")
            else: print(queue[0])
        elif line.strip() == "size":
            print(len(queue))
        elif line.strip() == "clear":
            queue = []; print("ok")
        else:
            command, value = line.strip().split()
            queue.append(int(value))
            print("ok")
    

if __name__ == "__main__":
    main()