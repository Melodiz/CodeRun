def main():
    with open("input.txt", "r") as file:
        text = []
        df = dict()
        for line in file.readlines():
            text.extend(list(map(str.strip, line.strip().split()))) 
        for i in range(len(text)):
            print(df.get(text[i], 0), end=" ")
            df[text[i]] = df.get(text[i], 0) + 1

    
if __name__ == "__main__":
    main()
