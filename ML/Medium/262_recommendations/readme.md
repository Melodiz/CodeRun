# [262. Лента рекомендаций](https://coderun.yandex.ru/problem/recommendations)

## Description

Рассмотрим ленту рекомендаций разнородного контента. В ней смешаны объекты разного типа (картинки, видео, новости и т.д.). Эти объекты обычно упорядочиваются по релевантности: чем релевантнее (интереснее) объект пользователю, тем он ближе к началу списка рекомендаций. При таком упорядочивании в списке рекомендаций часто встречается несколько объектов одного типа подряд. Рекомендации кажутся однообразными и поэтому не нравятся пользователям. Необходимо реализовать алгоритм, который по списку рекомендаций составит новый список — лишённый этого недостатка и при этом максимально релевантный.

Пусть задан исходный список рекомендаций $a = [a_0, a_1, \ldots, a_{n-1}]$ длиной $n \gt 0$. Объект под номером $i$ имеет тип с номером $b_i \in \{0, \ldots, m-1\}$ и релевантность $r(a_i) = 2^{-i}$. Рассмотрим список, который получается из исходного выбором подмножества объектов и их перестановкой: $x = [a_{i_0}, a_{i_1}, \ldots, a_{i_{k-1}}]$ длины $k$ ($1 \le k \le n$). Список называется допустимым, если никакие два подряд идущих объекта в нем не совпадают по типу, т.е. $b_{i_j} \ne b_{i_{j+1}}$ для всех $j = 0, \ldots, k - 2$. Релевантность списка вычисляется по формуле $\sum_{j=0}^{k-1} 2^{-j} r(a_{i_j})$.

Вам нужно найти максимальный по релевантности список среди всех допустимых.

### Input Format:

В первой строке через пробел записаны числа $n$ и $m$ ($1 \le n \le 100\,000$, $1 \le m \le n$). В следующих $n$ строках записаны числа $b_i$ для $i=0, \ldots, n-1$ ($0 \le b_i \le m-1$).

### Output Format:

Выпишите через пробел номера объектов итогового списка: $i_0, i_1, \ldots, i_{k-1}$.



## Example Test Cases

### Example 1

**Input:**
```
1 1
0

```

**Output:**
```
0

```

### Example 2

**Input:**
```
2 2
1
1

```

**Output:**
```
0

```

### Example 3

**Input:**
```
10 2
1
1
1
0
0
1
0
1
1
1

```

**Output:**
```
0 3 1 4 2 6 5

```

**Tags**: machine learning

