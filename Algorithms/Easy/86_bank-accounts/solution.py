import sys
def main():
    df = {}
    for line in sys.stdin.readlines():
        line = line.strip().split()
        type = line[0]
        if type == 'BALANCE':
            print(df.get(line[1], "ERROR"))
        elif type == 'DEPOSIT':
            df[line[1]] = df.get(line[1], 0) + int(line[2])
        elif type == 'WITHDRAW':
            df[line[1]] = df.get(line[1], 0) - int(line[2])
        elif type == "TRANSFER":
            f, t, amount = line[1], line[2], int(line[3])
            df[f] = df.get(f, 0) - amount
            df[t] = df.get(t, 0) + amount
        elif type == "INCOME":
            for client, amount in df.items():
                if amount > 0:
                    df[client] = amount + int(amount * float(line[1]) / 100)

if __name__ == "__main__":
    main()

            