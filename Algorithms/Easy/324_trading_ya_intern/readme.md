# [324. Много стульев](https://coderun.yandex.ru/problem/trading-ya-intern)

## Description

«Где бы выгодно купить стулья, а потом выгодно их продать», — думал Остап после неудачной погони за 12 стульями.

Он решил подзаработать себе на билет до Рио продажей мебели. Прежде чем начать работу, он решил понаблюдать за происходящим и придумать, как побольше заработать.

Остап узнал, что в городе все продавцы продают только по одному стулу, и каждый покупатель готов купить не более одного. Всего он нашел $N$ предложений, стоимость стула у $i$-го из продавцов равна $A_i$ рублей, конечно, цены могут отличаться. Кроме того, он нашёл $M$ потенциальных покупателей, каждый из которых может купить стул не дороже $B_i$ рублей. При этом сам Остап может купить и продать любое количество товара.

Остап хочет получить наибольшую прибыль, поэтому он обратился за помощью к вам. Определите максимальную прибыль, которую он может получить.

### Input Format:

Первая строка входных данных содержит два целых числа $N$, $M$ ($1 \le N, M \le 10^5$) — количество предложений и количество потенциальных покупателей соответственно.

Вторая строка содержит $N$ целых чисел $A_i$ ($0 \le A_i \le 10^9$) — цены, по которым продавцы готовы продавать стулья.

Третья строка содержит $M$ целых чисел $B_i$ ($0 \le B_i \le 10^9$) — суммы, которые потенциальные покупатели готовы отдать при покупке стула.

### Output Format:

Выведите одно целое число, равное максимальной прибыли, которую Остап может получить.

## Примечание

Приведём сделки для примера 2, при котором Остап заработает 27 рублей.

Покупка: 2, Продажа: 18, Прибыль: 18 - 2 = 16

Покупка: 4, Продажа: 11, Прибыль: 11 - 4 = 7

Покупка: 5, Продажа: 9, Прибыль: 9 - 5 = 4

Суммарная прибыль: 16 + 7 + 4 = 27



## Example Test Cases

### Example 1

**Input:**
```
2 3
1 1
3 3 3

```

**Output:**
```
4

```

### Example 2

**Input:**
```
6 5
5 10 8 4 7 2
3 1 11 18 9

```

**Output:**
```
27

```

**Tags**: greedy, sort

