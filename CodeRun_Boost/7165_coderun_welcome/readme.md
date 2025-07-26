## 7165\. Welcome to the CodeRun World\!

### Problem Description

You thought you were just going to solve a problem, but you ended up in a completely different world — the world of CodeRun.

Coderun, a virtual cat and guardian of this world, greets you. He has long dreamed of meeting you, and now you are finally here\!

"You can program whatever you want," says Coderun. "Grow forests from binary trees, build rivers from data streams, and populate them with methods, operators, and functions. I'll show you everything and even introduce you to Princess Brace herself\!... But for now, let's get our paws dirty: you need to get used to your new abilities\!"

"Let's try to build something that you can't build in the real world?" he continues his speech. "For example, a huge chessboard\! Here in front of you are $N$ white and $M$ black tiles of size $1 \\times 1$. What do you think is the maximum possible side of a square chessboard that can be made from these tiles?"

### Input Format

The function takes 2 parameters as arguments:

  * An integer $n$ ($0 \\le n \\le 10^9$) — the number of white tiles.
  * An integer $m$ ($0 \\le m \\le 10^9$) — the number of black tiles.

It is guaranteed that $n+m \> 0$.

### Output Format

As an answer, your program should return a single integer — the maximum size of a square chessboard that can be made from the tiles.

### Note

A board of size $n \\times m$ will be called a chessboard if it consists of $n$ rows and $m$ columns of unit cells, colored in a checkerboard pattern.

A checkerboard pattern is a coloring of cells in white and black, such that for any cell $(x, y)$, it is true that all existing adjacent cells $(x', y')$ are colored in a color different from the color of cell $(x, y)$.

### Constraints

  * Time limit: 2 seconds
  * Memory limit: 256 MB

### Example 1

**Input**

```
9
8
```

**Output**

```
4
```

### Example 2

**Input**

```
12
15
```

**Output**

```
5
```