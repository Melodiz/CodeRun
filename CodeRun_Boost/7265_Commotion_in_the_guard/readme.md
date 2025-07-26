## 7265\. Rearrangement in the Honor Guard

### Problem Description

Great\! You've managed to restore the bridge and get to the palace. In front of the gates — an honor guard: on the left, $2 \\times n$ guards are lined up, and on the right, the palace's function. All of them are in full dress uniform, glistening and standing strictly at attention.

But suddenly, something strange happens. The guards begin to randomly change places. Someone wants to swap with someone on the other side, someone is returning. And now it's completely unclear how many methods remained on their side, and how many on the right.

Coderun carefully observes every movement and asks for your help:
— Help me understand how many methods are currently on the left side? And that means — how many functions are on the right side?

So, at the entrance to the castle stood $2 \\times n$ guards:

  * $n$ methods, with numbers from 1 to $n$.
  * and $n$ functions, with numbers from $n+1$ to $2n$.

Initially, each guard stood at a position equal to their number.

$m$ permutations occurred. In each permutation, guards standing at positions $i\_k$ and $j\_k$ swapped places.

After each permutation, determine how many methods (with numbers from 1 to $n$) are currently in the left part of the line (at positions from 1 to $n$).

### Input Format

The function takes 3 parameters as arguments:

  * An integer $n$ ($1 \\le n \\le 100,000$) — the number of methods and functions in the honor guard (total $2n$ guards).
  * An integer $m$ ($1 \\le m \\le 100,000$) — the number of permutations that occurred in a row.
  * A one-dimensional array `swaps` ($1 \\le \\text{swaps}\_i \\le 2n$) of size $2m$ — elements with numbers $2(i-1)$ and $2(i-1)+1$ specify the $i$-th ($1 \\le i \\le m$) guard swap.

### Output Format

Output $m$ integers — one per line. Each integer should reflect how many methods (with numbers from 1 to $n$) are in the left part of the line (at positions from 1 to $n$), after each permutation.

### Constraints

  * Time limit: 2 seconds
  * Memory limit: 256 MB

### Example 1

**Input**

```
5
6
2 6
4 7
1 3
7 2
7 9
3 9
```

**Output**

```
4
3
3
4
4
3
```

### Example 2

**Input**

```
3
3
3 4
4 5
5 3
```

**Output**

```
2
2
3
```