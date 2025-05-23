# Нормализация показателей

Problem ID: normalization-of-indicators

URL: https://coderun.yandex.ru/problem/normalization-of-indicators/

Tags: binary search, sort

Разработчики сервиса сбора данных решили уменьшить количество возможных вариантов ответов. Для этого выбрали $n$ различных целых чисел — канонические варианты.

Но в системе уже имеется $m$ старых ответов. Для каждого их этих $m$ чисел необходимо найти ближайший из $n$ канонических вариантов, т.е. с минимальным модулем разности.


## Формат ввода

В первой строке записано целое число $n$ ($1 \le n \le 50\,000$).

Во второй строке записаны $n$ целых чисел $a_1$ $a_2$ … $a_n$ — канонические ответы.

В третьей строке записано одно целое число $m$ ($1 \le m \le 50\,000$).

В $j$-й из следующих $m$ строк записано одно целое число $b_{j}$.

Гарантируется, что все входные числа не превосходят $10^{6}$ по абсолютной величине.


## Формат вывода

Для каждого значения $b_j$ найдите каноническое значение (ближайшее). Если оптимальных значений несколько, выведите любое из них.

