# Solution for https://coderun.yandex.ru/problem/cards/
from itertools import combinations
from tqdm import tqdm

def solution():
    cards = [x for x in range(2, 15)] + [x for x in range(2, 15)] \
            + [x for x in range(2, 15)] + [x for x in range(2, 15)]
    count = 0
    total = 0
    for combination in tqdm(combinations(cards, r=6)):
        total += 1
        if sum(combination) == 21:
            count += 1
    print(f"Total combinations: {round(count/total,6)}")


if __name__ == "__main__":
    solution()