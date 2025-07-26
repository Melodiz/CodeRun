## 7267\. Erased Leaderboard

### Problem Description

Finally, we made it to the palace\!

— "This is the hall of gamers," Coderun tells us. "Here, on each wall, the results of the best player for each game are engraved."

But suddenly, our "tour guide" freezes: a digit on one of the walls is simply erased\! Coderun asks you to try to restore the data.

We know that in this game, a player earns at least $m$ gold coins for completing a round. However, instead of some numbers, there are blanks. You need to restore the information as much as possible.

The table recorded how many gold coins the player had at the end of each of $n$ rounds: $p\_1, p\_2, \\dots, p\_n$. The missing values are marked as $-1$.

Determine if these data could have been real.

If yes, restore the missing values.

### Input Format

The function takes 3 parameters as arguments:

  * An integer $n$ — the number of entries ($1 \\le n \\le 1000$).
  * An integer $m$ — the lower bound on the number of coins after completing each round ($0 \\le m \\le 100$).
  * A one-dimensional array of integers $p$ of size $n$: $p\_1, p\_2, \\dots, p\_n$ ($-1 \\le p\_i \\le 10^9$), where $p\_i$ means the number of coins the player had at the end of the $i$-th round. If the number is unreadable, then $p\_i = -1$.

### Output Format

As an answer, your program should return a one-dimensional array:

  * If the entries in the table cannot correspond to the amount of gold coins, you need to return an array of size 1 containing the single number $-1$.
  * If a solution exists, return an array of size $n$ of integers $a\_i$ — the number of gold coins the player earned at the end of the $i$-th round ($a\_i \\ge m$). If several answers exist, return any.

### Note

In the first example, there is a unique suitable sequence, as all numbers are readable and satisfy the requirement for $m$.

In the second example, both numbers are unreadable, so any sequence satisfying the requirement for $m$ will work.

In the third test case, it's impossible to get a sum equal to 5 from four numbers, each of which is at least 2.

### Constraints

  * Time limit: 2 seconds
  * Memory limit: 256 MB

### Example 1

**Input**

```
3
1
1 2 3
```

**Output**

```
1 1 1
```

### Example 2

**Input**

```
2
0
-1 -1
```

**Output**

```
0 0
```

### Example 3

**Input**

```
4
2
-1 -1 1 5
```

**Output**

```
-1
```