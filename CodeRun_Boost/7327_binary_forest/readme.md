## 7327\. In the Binary Forest

### Problem Description

Having crossed the river, Coderun plunged into the binary forest and has already found a path that needs to be followed to catch the enemy. You just can't escape him\! He immediately noticed a parallel path.

Unfortunately, carbon-based life forms cannot interfere in the binary world. But we can help Coderun\!

Both paths are represented by binary sequences of lengths $n$ and $m$.

To continue the chase, you need to understand how far they can go "on foot". For this, you need to find the maximum length of a non-decreasing common subsequence that can be obtained by crossing out some elements from both sequences.

### Input Format

The function takes 4 parameters as arguments:

  * An integer $n$ ($1 \\le n \\le 2 \\cdot 10^5$) — the number of elements in the first sequence.
  * A one-dimensional array of integers $a$ of size $n$ ($0 \\le a\_i \\le 1$) — elements of the first sequence.
  * An integer $m$ ($1 \\le m \\le 2 \\cdot 10^5$) — the number of elements in the second sequence.
  * A one-dimensional array of integers $b$ of size $m$ ($0 \\le b\_i \\le 1$) — elements of the second sequence.

### Output Format

As an answer, your program should return a single integer — the length of the longest common non-decreasing subsequence of the given sequences.

### Note

A subsequence $Q$ of a sequence $S$ of length $k$ is a set of values located at a subset of ordered indices:
$Q = {S\_{i\_1}, S\_{i\_2}, \\dots, S\_{i\_p}}$, where:

  * $1 \\le i\_1 \< i\_2 \< \\dots \< i\_p \\le k$
  * $p$ — the length of the subsequence.

A common subsequence $CQ$ of two sequences $A$ and $B$ is a subsequence that is both a subsequence of $A$ and a subsequence of $B$ (not necessarily at the same positions).

In the test case, the longest common non-decreasing subsequence of the given sequences is ${0, 0, 1, 1, 1}$:

  * It has length 5.
  * In sequence $A$, it is located at positions $[1, 2, 4, 6, 7]$.
  * In sequence $B$, it is located at positions $[1, 2, 3, 4, 6]$.

### Constraints

  * Time limit: 2 seconds
  * Memory limit: 256 MB

### Example 1

**Input**

```
7
0 0 0 1 0 1 1
6
0 0 1 1 0 1
```

**Output**

```
5
```