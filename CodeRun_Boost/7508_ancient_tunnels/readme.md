# 7508. Древние тоннели

🟢 Решена ⚪ Средняя

Ура, Кодерун вернулся!

Ты его нашёл! Наконец-то! Теперь всё наладится!

— Я упустил злодея. Но я узнал, кто это. Это CTRodent — артефакт старой версии системы. Он хочет вернуть 32-битную архитектуру. А для этого он собирается полностью снести весь этот мир!

Кодерун смог выяснить коварный план CTRodent'а. Негодяй собирается пробраться во дворец по древним, построенным ещё в эпоху dial-up'а, однонаправленным подземным тоннелям.

Подземелье представляет из себя $n$ ($1 \le n \le 2 \cdot 10^5$) различных комнат, соединенных однонаправленными тоннелями. Комнаты можно проходить исключительно в определенном порядке, заданном массивом $a$ размера $n$. Из комнаты с номером $i$ можно попасть в комнату с номером $a_i$. Если $a_i = -1$ (тупиковая комната) или $a_i$ уже посещалась, то дальше продолжать движение нельзя.

Чтобы перекрыть пути доступа к дворцу, нужно выяснить для каждого $i$, сколько существует различных маршрутов в подземелье, оканчивающихся в $i$-ой комнате, если начать можно из любой комнаты. Способы прохождения считаются различными, если они содержат различные комнаты или если порядок комнат отличается.

## Формат ввода

Каждый тестовый состоит из нескольких наборов входных данных. Первая строка содержит количество наборов входных данных $T$ ($1 \le T \le 3 \cdot 10^4$). Далее следует описание наборов входных данных.

Первая строка каждого набора входных данных содержит целое число $n$ ($1 \le n \le 2 \cdot 10^5$).
Вторая строка содержит $n$ целых чисел — описание массива $a_i$ ($a_i = -1$ или $1 \le a_i \le n, a_i \neq i$).

Гарантируется, что сумма $n$ по всем наборам входных данных не превышает $2 \cdot 10^5$.

## Формат вывода

Для каждого набора входных данных в отдельной строке выведите $n$ целых чисел, где $i$-е число обозначает количество различных способов прохождения, оканчивающихся $i$-ой комнатой.

## Примечание

В первом наборе входных данных для $i = 1$ есть только один вариант — начать с 1-ой комнаты.

Во втором наборе входных данных есть два варианта дойти до первой комнаты: 1, 2 -> 1; и для второй комнаты: 2, 1 -> 2.

В третьем наборе входных данных есть три варианта дойти до 2-ой комнаты:
* 1 -> 2, 3 -> 2, 2;
* и по одному для первой и третьей комнат (1 и 3 соответственно).

## Ограничения

Ограничение времени | 2 с
---|---
Ограничение памяти | 256 МБ

## Пример 1

### Ввод
```

6
1
\-1
2
1
\-1
3
2 1
\-1 2
4
2 4 2 -1
5
3 5 -1 2 4
7
3 -1 1 -1 4 5 -1

```

### Вывод
```

1
2 2
1 3 1
1 3 1 4
1 3 2 3 3
2 1 2 3 2 1 1

```