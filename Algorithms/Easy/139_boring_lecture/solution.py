# Solution for https://coderun.yandex.ru/problem/boring-lecture/

def main():
    word = input(); n = len(word)
    count_letters = dict([(letter, 0) for letter in word])
    for i in range(n):
        count_letters[word[i]] += (i+1)*(n-i)
    for letter, count in sorted(count_letters.items()):
        print(f"{letter}: {count}")


if __name__ == "__main__":
    main()
