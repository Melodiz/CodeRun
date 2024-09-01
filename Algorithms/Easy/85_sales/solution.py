import sys


def main():
    data = {}
    for line in sys.stdin.readlines():
        line = line.strip().split()
        client, type, amount = line[0], line[1], int(line[2])
        if client not in data:
            data[client] = {}
        data[client][type] = data[client].get(type, 0) + amount

    clinets = sorted(data.keys())
    for client in clinets:
        types = sorted(data[client].keys())
        print(client + ":")
        for type in types:
            print(type, data[client][type])
    return 0


if __name__ == "__main__":
    main()
