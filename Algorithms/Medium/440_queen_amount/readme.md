# [440. У кого больше королев?](https://coderun.yandex.ru/problem/queen-amount)

## Description

In a distant country, players gathered to play an exciting card game. Their deck consisted of 54 cards, including 4 cards of each suit from 2 to King, as well as 2 jokers. Players received 13 cards each, and two cards went into the discard pile.

After the cards were dealt, players in turn declared how many kings they had. However, it is unknown which of them could have lied.

You need to find out the minimum number of players who could have lied about the number of kings.

### Input Format:

The single line of the input file contains 4 integers $a, b, c, d$ ($0 \le a, b, c, d \le 9$) - the number of kings declared by each player, in their own words.

### Output Format:

Output a single number - the minimum number of players who could have lied.

## Примечание

In the first example, according to the players, they collectively had 10 kings. At least two players lied. For example, it is also possible that the first player had 0 kings, the second 2, the third 1, and the fourth 1. Then the first and third players lied.

In the second example, each player could have had one king, and in that case, the fourth player lied.

In the third example, a card distribution is possible where no one lied.

## Example Test Cases

### Example 1

**Input:**
```
3 2 4 1

```

**Output:**
```
2

```

### Example 2

**Input:**
```
1 1 1 2

```

**Output:**
```
1

```

### Example 3

**Input:**
```
1 1 1 1

```

**Output:
```
0

```