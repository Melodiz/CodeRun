import sys
def main():
    # read all lines from stdin
    data = sys.stdin.readlines()
    ans = set()
    for line in data:
        # split each line into words
        words = line.strip().split()
        # add each word to the set
        for word in words:
            ans.add(word.strip())
    print(len(ans))

if __name__ == "__main__":
    main()