## 7268\. Key to the Magic Door

### Problem Description

You were so engrossed in restoring the leaderboard that you almost forgot why you are here\! Coderun pulls you aside, towards the ballroom, and suddenly you notice an inconspicuous door in the wall. Worn, without handles, with a dull symbol $\\partial$ carved directly into the stone.

— "This door hasn't been opened for a very long time," Coderun says quietly. "An ancient algorithmist named Divizor created it. No one knows for sure what opens it, but it's probably possible to open it using sequences of simple numbers. Want to try?"

Coderun runs his paw over the door — and strings appear on its surface:

For a natural number $n$ ($2 \\le n \\le 2 \\cdot 10^6$), find the number of strictly increasing sequences of distinct prime numbers $q\_1, q\_2, \\dots, q\_k$, such that:

  * All elements $q\_i$ are prime numbers;
  * The length of the sequence $k = q\_1 + 1$;
  * The sum $(q\_2 + q\_3 + \\dots + q\_k)$ is divisible by $q\_1$ without a remainder.

The key is a single number. The number of such sequences.

### Input Format

The function takes 1 parameter as an argument:

  * An integer $n$ ($2 \\le n \\le 2 \\cdot 10^6$) — the given natural number.

### Output Format

As an answer, your program should return a single integer — the number of sequences that satisfy the problem's conditions.

### Note

For the second test, possible prime numbers: 2, 3, 5.
Let's look at all possible $q\_1$:

  * $2: k = 2 + 1 = 3$, sequence: $3 + 5$ is divisible by 4 without a remainder.
  * $3, 5$: for the given constraints, we cannot construct a sequence of length $q\_1 + 1$.
    Answer for this test: 1.

For the third test, there are 2 correct sequences: 2, 3, 5 and 2, 5, 7.

### Constraints

  * Time limit: 2 seconds
  * Memory limit: 256 MB

### Example 1

**Input**

```
3
```

**Output**

```
0
```

### Example 2

**Input**

```
5
```

**Output**

```
1
```

### Example 3

**Input**

```
7
```

**Output**

```
2
```