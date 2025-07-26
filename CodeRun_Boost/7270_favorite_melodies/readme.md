## 7270\. Princess Brace's Favorite Melodies

### Problem Description

The garden came alive — flowers burst forth from gray slabs, walls were covered with a mosaic of leaves, and the ceiling blossomed with digital clouds and light. Everything around turned green, stirred, sang...

But suddenly — a sudden noise from the ballroom. Has something happened again?

The orchestra was preparing to play the princess's favorite compositions. But alas\! Someone has shuffled all the sheet music pages. Now the musicians don't know which pages to play — after all, each of them reflects how much the princess likes a certain segment of the melody.

We know that Princess Brace makes exactly $q$ musical requests. Each request is a range from page $l$ to page $r$ inclusive.

On each page, there is a number indicating its "affection" to this fragment. However, the order of the pages can be changed.

Your task is to rearrange all $n$ sheet music pages so that the total joy of the princess from all played orchestral excerpts is maximized.

### Input Format

The first two arguments of the function are integers $n$ and $q$ ($1 \\le n, q \\le 10^5$).

The third argument is an array of $n$ integers $a\_i$, specifying the princess's "affection" to page number $i$ ($1 \\le a\_i \\le 10^9$).

The fourth argument is an array of $q$ pairs of integers $l, r$ ($1 \\le l \\le r \\le n$), denoting the princess's requests.

### Output Format

Return the maximum possible total joy of the princess from the played orchestral excerpts after rearranging the pages in the function.

### Constraints

  * Time limit: 2 seconds
  * Memory limit: 256 MB

### Example 1

**Input**

```
3 4
7 3 1
1 3
1 2
3 3
2 2
```

**Output**

```
31
```

### Example 2

**Input**

```
4 4
1 100 10000 101010
1 4
2 3
2 2
1 2
```

**Output**

```
40424241
```