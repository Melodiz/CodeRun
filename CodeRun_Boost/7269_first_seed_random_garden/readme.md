## 7269\. First Seed in a Random Garden

### Problem Description

With a creak, the door opens, and Coderun freezes in delight:
— "It's... the Random Garden\!" — he whispers, shocked. "And I thought it didn't exist\!"

Before you is a gray floor. Gray walls. Gray ceiling. Even the window is gray. The most boring room in the world.

— "My dear, are you lost?" — Coderun raises an eyebrow. — "The Random Garden is a generative ecosystem, built into the castle's core. It blossoms anew each time, depending on which seed is passed to the kernel. Want to see how it blossoms? Try to calculate the value of a recursive function."

Elements of the sequence $a\_n$ ($1 \\le n \\le 10^{18}$) are integers and can be calculated by the following recursive formula:

$a\_n = (a\_{n/2}^3 + 5 \\cdot a\_{n/4} + n) % (10^9 - 7538)$, where:

  * $a\_0 = 1$,
  * $u % v$ means the remainder of division of $u$ by $v$,
  * $//$ means integer division.

Find the last element of the sequence $a$ and see how the Random Garden blossoms.

### Input Format

The function takes 1 parameter as an argument:

  * An integer $n$ ($1 \\le n \\le 10^{18}$) — the index of the last element of the sequence.

### Output Format

As an answer, your program should return a single integer — the value of $a\_n$.

### Note

  * In the first example, $a\_1 = 1^3 + 5 \\cdot 1 + 1 = 7$.
  * In the second example, $a\_5 = a\_{5/2}^3 + 5 \\cdot a\_{5/4} + 5 = a\_2^3 + 5 \\cdot a\_1 + 5 = 14^3 + 40 = 105413544$.

### Constraints

  * Time limit: 1 second
  * Memory limit: 32 MB

### Example 1

**Input**

```
1
```

**Output**

```
7
```

### Example 2

**Input**

```
5
```

**Output**

```
105413544
```

### Example 3

**Input**

```
100
```

**Output**

```
464980765
```