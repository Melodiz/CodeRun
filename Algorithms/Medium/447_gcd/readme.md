# [447. НОД](https://coderun.yandex.ru/problem/gcd)

## Problem Statement

You are required to find the GCD (Greatest Common Divisor) of two numbers, A and B. Formally, this is the largest number C that divides both A and B without a remainder.

In this problem, the numbers A and B are very large and do not fit into standard data types. For this reason, they are defined by the sequences of their factors $a_1, \dots, a_n$ and $b_1, \dots, b_m$. We define $A = \prod_{i=1}^{n} a_i$ and $B = \prod_{i=1}^{m} b_i$.

---

## Input Format

* The first line contains an integer `n` ($1 \le n \le 1000$).
* The second line contains `n` integers $a_i$ ($1 \le a_i \le 10^9$) separated by spaces.
* The third line contains an integer `m` ($1 \le m \le 1000$).
* The fourth line contains `m` integers $b_i$ ($1 \le b_i \le 10^9$) separated by spaces.

---

## Output Format

Print the last 9 digits of the greatest common divisor of A and B. Note that leading zeros must be printed if the full result contains more than 9 digits, but they are not needed if the answer itself has fewer than 9 digits.

---

## Constraints

* **Time Limit:** 1 second
* **Memory Limit:** 256 MB

---

## Example 1

### Input
```
3
2 3 5
2
4 5
```

### Output
```
10
```
*Explanation: A = 2 * 3 * 5 = 30. B = 4 * 5 = 20. GCD(30, 20) = 10.*