# [5316. Снежки](https://coderun.yandex.ru/problem/snowballs)

## Description

On a New Year's morning, Koderyn and a friend molded snowballs and invented a game. Initially, players have three piles of snowballs. On their turn, a player can take one or two snowballs from any one of the piles, provided there is a sufficient number of snowballs in the pile. Taken snowballs are set aside and not considered further.

The player who cannot make a move loses.

For given sizes of three piles, determine who wins with optimal play from both players – the one who moved first, or the one who moved second. You need to answer $t$ independent queries. For each query, output 1 if the first player wins for the given pile sizes, and 0 otherwise. Output the answers to the queries in the order they appear in the input data.

### Input Format:

The first line of the input file contains a single integer $t$ ($1 \le t \le 10$) – the number of queries. The following $t$ lines contain the queries themselves.

Each query is described by three integers $0 \le a_1, a_2, a_3 \le 10^9$ – the sizes of the piles.

### Output Format:

For each query, output 1 if the first player wins for the given pile sizes, and 0 otherwise.

## Example Test Cases

### Example 1

**Input:**
```
2
1 3 5
0 0 3
```

**Output:**
```
1
0
```