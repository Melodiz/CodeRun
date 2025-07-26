## 7266\. Staircase with a Trick

### Problem Description

Phew, that wasn't easy, but the methods and functions are lined up again in the honor guard, the palace doors are wide open\!... All that's left is to go up the wide ceremonial staircase.

— Oh no, what is this? The staircase is broken\! Each step should be higher than or at least the same height as the previous one, so that climbing is comfortable and safe. But someone has maliciously changed the heights of the steps\!

— "Someone is trying to spoil our holiday..." — Coderun is disappointed.

Maybe you can fix the staircase?

You can flip a step by simply changing the sign of its height: any step with height $a\_i$ can be turned into $-a\_i$.

You need to figure out if it's possible to fix the staircase so that its heights are non-decreasing.

### Input Format

The function takes 2 parameters as arguments:

  * An integer $n$ — the number of steps ($1 \\le n \\le 100,000$).
  * A one-dimensional array of integers $a$ ($|a\_i| \\le 100,000$) — an array of step heights.

### Output Format

As an answer, your function should return an array `result` of size $n+1$, where:

  * `result[0] = 0` if no solution exists, `result[0] = 1` otherwise.
  * If a solution exists: `result[1...n]` contains $n$ numbers `result[i]` that form a non-decreasing array, and for all $1 \\le i \\le n$, `result[i] = a_i` or \`result[i] = -a\_i$.

### Constraints

  * Time limit: 2 seconds
  * Memory limit: 256 MB

### Example 1

**Input**

```
5
1 -1 -2 3 6
```

**Output**

```
Yes
-1 -1 2 3 6
```

### Example 2

**Input**

```
3
1 1 0
```

**Output**

```
Yes
-1 -1 0
```

### Example 3

**Input**

```
10
-35808 88285 25933 -88676 -14525 11664 -14736
```

**Output**

```
No
```