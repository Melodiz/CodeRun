# Кубики

Problem ID: cubes

URL: https://coderun.yandex.ru/problem/cubes/

Tags: standard library, two pointers, set

Аня и Боря любят играть в разноцветные кубики, причём у каждого из них свой набор и в каждом наборе все кубики различны по цвету. Однажды дети заинтересовались, сколько существуют таких цветов, что кубики каждого цвета присутствуют в обоих наборах. Для этого они занумеровали все цвета случайными числами. На этом их энтузиазм иссяк, поэтому вам предлагается помочь им в оставшейся части.
Номер любого цвета — это целое число в пределах от 0 до $10^9$.


## Формат ввода

В первой строке входного файла записаны числа N и M (1 $\le$ N, M $\le$ 100000) — количество кубиков у Ани и Бори
соответственно. В следующих N строках заданы номера цветов кубиков Ани. В
последних M строках  номера цветов кубиков Бори.


## Формат вывода

Выведите сначала количество, а затем отсортированные по возрастанию номера цветов
таких, что кубики каждого цвета есть в обоих наборах, затем количество
и отсортированные по возрастанию номера остальных цветов у Ани, потом количество и
отсортированные по возрастанию номера остальных цветов у Бори.

