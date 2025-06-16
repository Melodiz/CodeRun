# [586. Число](https://coderun.yandex.ru/problem/number)

## Description

Вводится одно целое число $N$. Выведите его и фразу "I got it".

### Input Format:
Одно целое число $N$.

### Output Format:
Сначала фраза "I got it", затем число $N$.

## Example Test Cases

### Example 1

**Input:**
```
1

```

**Output:**
```
I got it
1

```

### Example 2

**Input:**
```
7

```

**Output:**
```
I got it
7

```

**Tags**: ad hoc, math, implementation

# Solution Comments:
Core Idea is: we don't need to find the smallest such number, just any. Therefore let's use N as building blocks to construct required M. For example if N = 123 then 123123123123 is N*100100100100 which is garanteed to be a multiple of N. In such M, which constructed on k blocks (int(k * str(N))) sum of it's degits = k * sum_of_digits(N), therefore let's k = N/gcd(S, N) and we garantee to satify the problem.