## 7328\. Game Field

### Problem Description

Night has fallen, and Coderun still hasn't returned. What to do now? "Excuse me, could you move?" — A man stretches out a hand with tiles towards you from behind a huge backpack. He silently puts the tiles on the ground and starts laying them out. — "You're playing a game on my field. And I need to arrange the tiles. It's a new field for Minesweeper. Every day I collect thousands of them — for over 40 years. And people just don't have enough." He doesn't seem worried. He has a task. A regular routine.

— "Isn't it complex?" — A person extends tiles. — "No, it's very simple, just very complex. Right now, little mine means a more interesting game."

You take the tiles. What to do? It's not entirely clear where to go next. All you need to do is fill a square $N \\times N$ field so that the sum of numbers on empty cells in this arrangement is maximum...

Here is a formal description:

Given an $N \\times N$ field. In some cells of the field there are mines, and the player does not know where they are. The player chooses each cell and finds out what is behind it. If there is a mine in the given cell, the player immediately loses. Otherwise, the cell displays a number that indicates how many mines are among the 8 neighboring cells (neighbors by side or by vertex).

After the game ends, regardless of the mines, the entire field is revealed with numbers and mines. The larger the sum of numbers for a specific mine arrangement, the more complex the game is.

For a given $N$, find which arrangement is the most complex. If there are several such arrangements, any will do.

### Input Format

Your function takes 1 parameter as an argument:

  * An integer $N$ ($1 \\le N \\le 5 \\cdot 10^3$) — the side length of the square tile field.

### Output Format

Your function should return an object with two fields (see template):

  * `sum` - the maximum possible sum of numbers on empty cells of an $N \\times N$ board with the best mine arrangement.
  * `field` - an array of $N$ strings, representing the best arrangement with the sum `sum`.
    Each string in `field` represents one row of the desired arrangement:
  * `|field|_i| = N` for $i \\in [1, N]$;
  * `field_i` contains only the characters "X" (mine) and "-" (empty cell).

If there are several best arrangements with the maximum sum of numbers, return any.

### Constraints

  * Time limit: 1 second
  * Memory limit: 256 MB

### Example 1

**Input**

```
1
```

**Output**

```
0
X
```

### Example 2

**Input**

```
2
```

**Output**

```
4
X-
-X
```