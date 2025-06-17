# Solution for https://coderun.yandex.ru/problem/additional-check-cheating
# Other solutions: https://github.com/Melodiz/CodeRun
from collections import Counter
import re


def read_data():
    with open("input.txt", "r") as f:
        n, c, d = f.readline().split()
        banned_words = set([f.readline().strip() for _ in range(int(n))])
        text = f.read()
    return n, c, d, banned_words, text


def main():
    n, c, d, banned_words, text = read_data()
    # find all words in text
    if c == 'no':
        text = text.lower()
        banned_words = [word.lower() for word in banned_words]

    words = re.findall(r'\b\w+\b', text)
    words = [word for word in words if word not in banned_words]
    if d == 'no':
        words = [word for word in words if word[0].isalpha()]
    else:
        words = [word for word in words if not word.isnumeric()]
    print(Counter(words).most_common(1)[0][0])


if __name__ == "__main__":
    main()
