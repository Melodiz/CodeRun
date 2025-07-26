## 7264\. Bridge to the Palace

### Problem Description

You've acquired new abilities. Pretty cool, huh? Well, I'll show you even more, but first, you need to hurry to the royal palace: Princess Brace is hosting a ball today\!

...Oh, what's this? The bridge leading to the princess's palace is destroyed\! Just recently, memory blocks were hanging over the river, but now they are scattered along the number line.

To get to the palace, you need to restore the bridge by moving blocks so that they are continuously arranged one after another.

How many movements do you think you'll need to restore the bridge?

### Input Format

The first argument of the function $N$ — the number of blocks ($1 \\le N \\le 10^5$).

The second argument of the function is an array of $N$ integers $a\_i$ — the coordinates of the points where the blocks are located ($-10^9 \\le a\_i \\le 10^9$). It is guaranteed that each point contains no more than one block.

### Output Format

The function should return the minimum number of block movements required to arrange all $N$ blocks in $N$ points with consecutive coordinates.

### Note

In the first example, the following movements are suitable:

  * Move block from point -3 to point 1
  * Move block from point 6 to point 4

After this, all blocks will be located in consecutive points with numbers from 0 to 4.

### Constraints

  * Time limit: 2 seconds
  * Memory limit: 256 MB

### Example 1

**Input**

```
5
2 0 -3 3 6
```

**Output**

```
2
```

### Example 2

**Input**

```
1
25
```

**Output**

```
0
```