# [290. Игра](https://coderun.yandex.ru/problem/game)
## Description

Basya, in his free time from programming, loves to play a self-invented game called "Life".

The game takes place on a field consisting of $n \times m$ identical cells. For convenience, Basya numbers all rows with integers from $1$ to $n$ from top to bottom, and also numbers all columns with integers from $1$ to $m$ from left to right.

Basya counts as neighbors those cells of the field that have a common edge.

The game process consists of $k$ iterations. In each iteration of the game, each cell of the field is in one of three states:
1. Inactive. Basya marks such a cell with the number 1.
2. Stable. Basya marks such a cell with the number 2.
3. Unstable. Basya marks such a cell with the number 3.

Basya calls active those cells of the field that are in a stable or unstable state.

Basya starts the game with a field, each cell of which is in some pre-selected initial state.

When transitioning to the next iteration of the game, Basya forms a new field, the state of each cell of which is assigned according to the following rules:
1. If the cell was inactive in the previous iteration, and at least one neighboring cell is in a stable state, then in the next iteration the cell will be in a stable state.
2. If the first rule is not met, and at least one neighbor is in an active state, then in the next iteration the cell will be in an unstable state.
3. If the previous rules are not met, then in the next iteration the cell will be in an inactive state.

Basya wants to plan for each cell how many state changes he will have to make by the end of the game. Since Basya has not yet had time to master all the intricacies of programming, he asks you for help in this task.

### Input Format:

The first line of input contains three integers $n, m, k$ ($1 \le n, m, k \le 100$).
The following $n$ lines describe the state of each cell of the initially selected field by Basya. The $i$-th ($1 \le i \le n$) of these lines contains $m$ integers — $a_{i1}, \dots, a_{im}$, where $a_{ij} \in \{1, 2, 3\}$ — the state of the cell in row $i$ and column $j$ of the initially selected field by Basya.
All numbers in each row are separated by exactly one space.

### Output Format:

In the $i$-th ($1 \le i \le n$) row of output, you need to output $m$ integers — $b_{i1}, \dots, b_{im}$, where $b_{ij}$ — the number of state changes for the cell in row $i$ and column $j$.

## Примечание

In the first example, in each iteration, a cell in an inactive state (1) gets an unstable state (3), and a cell in an unstable state (3) gets an inactive state (1).

In the second and third examples, after the first iteration, all cells get an unstable state (3) and no longer change their state.

## Example Test Cases

### Example 1

**Input:**
```
2 2 2
3 1
1 3

```

**Output:**
```
2 2 
2 2 

```

### Example 2

**Input:**
```
2 3 3
1 2 3
3 2 1

```

**Output:**
```
1 1 0 
0 1 1 

```

### Example 3

**Input:**
```
1 10 4
1 2 3 3 2 1 1 2 3 3

```

**Output:**
```
1 1 0 0 1 1 1 1 0 0 

```

**Tags**: implementation

