# [289. Рулетка](https://coderun.yandex.ru/problem/roulette)

## Description

Petya and Vasya came to the casino and decided to play roulette. We will assume that the outcomes from 0 to 36 are equally probable (in our problem, the roulette is fair).

Petya wins one chip if the roulette lands on a number from $x$ to $y$ ($0 \\le x \\le y \\le 36$). Vasya wins one chip if the roulette lands on a number from $u$ to $v$ ($0 \\le u \\le v \\le 36$).

Friends played $k$ ($1 \\le k \\le 20$) rounds. Find the probability that Petya has $a$ chips and Vasya has $b$ chips ($0 \\le a, b \\le k$).

Note that in a single run, you need to process several test cases.

### Input Format:

The first line of input contains an integer $t$ ($1 \\le t \\le 100$) — the number of test cases.

Next follow the descriptions of the test cases. Each test case occupies one line. The line contains seven integers $k, x, y, u, v, a, b$.

### Output Format:

For each test case, output the required probability on a separate line. The answer should be correct if the absolute error does not exceed $10^{-6}$.

## Constraints

Time limit: 5c
Memory limit: 256MB

## Example Test Cases

### Example 1

**Input:**

```
3
5 0 27 34 35 2 2
5 10 20 0 15 1 0
5 13 19 1 9 3 3

```

**Output:**

```
0.009497006351
0.023627148938
0.000000000000

```

**Tags**: combinatorics, probability theory