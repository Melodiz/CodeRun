# 7509. Ядро в опасности

🟢 Решена ⚪ Сложная

Кажется, все тоннели к замку перекрыты. Ты и Кодерун направляетесь во дворец, чтобы доложить обстановку Принцессе Брейс. Но, войдя в тронный зал, замираете.

Принцесса сидит у королевского root-терминала. На ней нет лица. – Мы думали, он пытается прорваться в замок, – еле слышно говорит она. – Но он... он проник в самое ядро нашего мира. Кодерун бросается к терминалу:

– Ядро заражено. CTRodent внедрил вредоносную подпрограмму. Она выбирает произвольный участок массива и заменяет его на нейтральное значение MEX – минимальное неотрицательное число, которого не было в этом фрагменте. Мы не знаем, какой именно участок он изменил, но нам нужно оценить, как сильно повреждена структура ядра.

Более формально:

Дан массив $a$ из $n$ целых чисел.

Необходимо ровно один раз выбрать два целых числа $l$ и $r$ ($1 \le l \le r \le n$) и заменить все $a_i$ ($l \le i \le r$) на $MEX(a_l, a_{l+1}, \dots, a_r)$.

Ваша задача независимо найти четыре значения, а именно среди всех возможных массивов $m$ после ровно одного преобразования:

* Минимальное $\max(a)$
* Максимальное $\max(a)$
* Минимальное $\min(a)$
* Максимальное $\min(a)$

Где $\max(a)$ - максимальное значение в $a$, $\min(a)$ - минимальное.

## Формат ввода

Каждый тест состоит из нескольких наборов входных данных. Первая строка содержит количество наборов входных данных $T$ ($1 \le T \le 4 \cdot 10^4$).

Далее следует описание наборов входных данных.

Первая строка каждого набора входных данных содержит одно целое число $n$ ($1 \le n \le 2 \cdot 10^5$) — длину массива $a$.

Вторая строка содержит $n$ целых чисел $a_1, a_2, \dots, a_n$ ($0 \le a_i \le 10^9$) — элементы массива $a$.

Гарантируется, что сумма $n$ по всем наборам входных данных не превосходит $2 \cdot 10^5$.

## Формат вывода

Для каждого набора входных данных в отдельной строке выведите четыре целых числа через пробел:
* минимально возможное значение $\max(a)$,
* максимально возможное значение $\max(a)$,
* минимально возможное значение $\min(a)$,
* максимально возможное значение $\min(a)$

после ровно одного преобразования массива (каждое значение вычисляется независимо).

## Примечание

### Определения
$MEX$ множества чисел определяется как наименьшее целое неотрицательное число, которое не встречается в этом множестве.

Например, $MEX(1, 0, 4, 1, 2)$ равен $3$, а $MEX(2, 1, 3, 2)$ равен $0$.

### Тестовые примеры
В первом наборе входных данных есть только один вариант выбрать $l$ и $r$, после чего $a = [0]$ и все четыре значения равны $0$.

Во втором наборе входных данных массив $a$ после **ровно одного** преобразования может быть равен $[1, 1]$, $[0, 0]$ или $[2, 2]$.

Соответственно
* минимальное возможное значение $\max(a) = 0$;
* максимально возможное значение $\max(a) = 2$;
* минимальное возможное значение $\min(a) = 0$;
* максимально возможное значение $\min(a) = 2$.

## Ограничения

Ограничение времени | 2 с
---|---
Ограничение памяти | 256 МБ

## Пример 1

### Ввод
```

6
1
0
1
1
2
0 1
3
0 0 0
4
0 0 1 2
5
4 3 0 2 1
6
4 1 0 2 3 1

```

### Вывод
```

0 0 0 0
0 2 0 2
1 1 0 1
0 3 0 3
1 5 0 5
3 5 0 5

```