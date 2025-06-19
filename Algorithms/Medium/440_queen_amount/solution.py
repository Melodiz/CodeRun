# Solution for https://coderun.yandex.ru/problem/queen-amount
# Other solutions: https://github.com/Melodiz/CodeRun
from itertools import combinations

def main():

  claims = list(map(int, input().split()))

  TOTAL_KINGS = 4

  if 2<= sum(claims) <= TOTAL_KINGS:
    return 0

  for combo in combinations(claims, 3):
    if sum(combo) <= TOTAL_KINGS:
      return 1

  for combo in combinations(claims, 2):
    if sum(combo) <= TOTAL_KINGS:
      return 2

  for claim in claims:
    if claim <= TOTAL_KINGS:
      return 3

  return 4

if __name__ == "__main__":
  print(main())    