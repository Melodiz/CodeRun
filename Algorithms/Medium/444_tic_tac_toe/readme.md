# [444. Крестики-нолики](https://coderun.yandex.ru/problem/tic-tac-toe)

## Description

You are given a grid field of arbitrary size $n \times m$. On this field, Vasya and Petya drew tic-tac-toe. They were so carried away with drawing that they completely forgot the rules. They did not follow the order of moves and did not check if they won. They got tired of drawing and decided to finish the game.

You are required to check if the game is finished on this field. In this task, it is considered that a player wins in tic-tac-toe if their symbol appears 5 times in a row vertically, horizontally, or diagonally. Note that since Vasya and Petya did not follow the game, a situation is possible where both won.

### Input Format:

The first line of input contains two numbers $n, m$ ($1 \le n, m \le 1000$) - the size of the game field.
The next $n$ lines contain a textual description of the field: each line contains $m$ characters, each of which is one of three symbols: `.` `X` or `0`. These symbols correspond to an empty cell, a cell with a cross, and a cell with a naught, respectively.

### Output Format:

Output `Yes` if one of the players won, and `No` otherwise.

## Примечание

In the first test case, players placed their symbols in one line, and the naught player won by collecting five naughts in a row.

In the second test case, naughts won, filling the last column.

## Example Test Cases

### Example 1

**Input:**
```
2 5
XXXX.
OOOOO

```

**Output:**
```
Yes

```

### Example 2

**Input:**
```
5 6
XX...O
.XXXXO
.....O
.....O
.....O

```

**Output:**
```
Yes

```