## 7326\. Pursuit

### Problem Description

Thank you for your attentiveness and quick reaction\! Coderun has found strange ID repetitions and calculated the villain\!

There he is\! Caught him\! But where is he?

"Faster\!" shouts Princess Brace. "He's heading for the river\!"

You rush in pursuit. The enemy is racing away from the castle, heading towards the river. There's no bridge. Only a series of boulders leading across a turbulent river. This is your chance, but you'll have to jump precisely.

Coderun nods: "You can only jump 1 or 2 meters. And only onto stones. Stones are installed at pre-known coordinates. Get to the other bank $n$ — with the smallest number of jumps — from coordinate 0. And if there are several such paths, choose the one where the jumps are arranged in lexicographically minimal order."

Can you catch the enemy?

### Input Format

Your function takes 3 parameters as arguments:

  * Integers $n, k$ ($1 \\le n \\le 10^5$; $0 \\le k \< n$) — the coordinate to reach and the number of stones, respectively.
  * A one-dimensional array of $k$ integers $a\_i$ ($1 \\le a\_i \\le n$) — the coordinates of the stones.
    It is guaranteed that for all $i \> 1$, $a\_i \> a\_{i-1}$.

### Output Format

Your program should return an array:

  * If there is no answer, an array of length 1 containing -1.
  * If there is an answer, an array `res` of length `ans + 1`, where `res[0]` contains the length of the answer, and `res[1...ans]` — the jumps required to get from coordinate 0 to coordinate $n$ — a sequence of 1s and 2s.

The path must be minimal in length, and if there are several paths of minimal length — lexicographically minimal among them.

### Constraints

  * Time limit: 4 seconds
  * Memory limit: 256 MB

### Example 1

**Input**

```
5 3
2 3 4
```

**Output**

```
3
2
1
2
```

### Example 2

**Input**

```
7 3
2 3 4
```

**Output**

```
-1
```