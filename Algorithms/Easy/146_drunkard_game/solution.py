# Solution for https://coderun.yandex.ru/problem/drunkard-game
# Other solutions: https://github.com/Melodiz/CodeRun
from collections import deque

def main():
    first_cards = deque(map(int, input().split()))
    second_cards = deque(map(int, input().split()))

    for move in range(10**6+1):
        if not first_cards:
            print("second", move)
            return
        if not second_cards:
            print("first", move)
            return
        a = first_cards.popleft()
        b = second_cards.popleft()
        if (a == 0 and b == 9) or (a > b and not (a == 9 and b == 0)):
            first_cards.append(a)
            first_cards.append(b)
        else:
            second_cards.append(a)
            second_cards.append(b)
    print("botva")

if __name__ == "__main__":
    main()
