def max_index(data):
    m = float('-inf')
    max_index = 0
    for i in range(len(data)):
        if data[i] > m:
            m = data[i]
            max_index = i
    return max_index

def place(data, member):
    ans = 0
    for num in data:
        if num > member:
            ans += 1
    return ans + 1

def main():
    n = int(input())
    data = list(map(int, input().split()))
    k = max_index(data)
    candidates = []
    for i in range(k+1, len(data)-1):
        if (data[i] % 10 == 5) and (data[i + 1] < data[i]):
            candidates.append(data[i])
    if len(candidates) == 0:
        print(0)
    else:
        print(place(data, max(candidates)))

if __name__ == "__main__":
    main()