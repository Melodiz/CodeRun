# [22. Минимум на отрезке](https://coderun.yandex.ru/problem/minimum-of-the-segment)

## Description

Consider a sequence of integers of length $n$.

A "window" of length $k$ moves along it: initially, the window contains the first $k$ numbers, in the next step the window will contain $k$ numbers starting from the second, and so on until the end of the sequence.

For each position of the "window", it is required to determine the minimum value within it.

### Input Format:

The first line of the input data contains two natural numbers $n$ and $k$ ($n \\le 150000, k \\le 10000, k \\le n$) — the lengths of the sequence and the "window", respectively.

The next line contains $n$ integers — the sequence itself.

### Output Format:

Output $n - k + 1$ lines. Each line should contain a single number — the minimum for the corresponding "window" position.

## Example Test Cases

### Example 1

**Input:**

```
7 3
1 3 2 4 5 3 1

```

**Output:**

```
1
2
2
3
1

```

**Tags**: deque, heap