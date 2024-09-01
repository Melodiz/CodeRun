from collections import Counter
def main():
    genA = input()
    genB = input()
    list_1 = []
    list_2 = []
    for i in range(len(genA)-1):
        list_1.append(genA[i]+genA[i+1])
    counter_a = Counter(list_1)
    del genA, list_1

    for j in range(len(genB)-1):
        list_2.append(genB[j]+genB[j+1])
    counter_b = set(list_2)
    del genB, list_2

    ans = 0
    for key in counter_a.keys():
        if key in counter_b:
            ans += counter_a[key]
    print(ans)

if __name__ == "__main__":
    main()