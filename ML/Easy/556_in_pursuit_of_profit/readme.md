# [В погоне за прибылью](link)

## Description

В городе N-ске есть район, в котором находятся n домов. Дома в районе распределены так, что некоторые из них образуют плотные кварталы, являющиеся выпуклой фигурой. Всего в районе $k$ кварталов. Вам нужно разместить $k$ пунктов выдачи заказов так, чтобы максимизировать их прибыль.

Считаем, что ожидаемая прибыль открытия $q$ пунктов выдачи равна:

$C-\sum_{i=0}^q\sum_h^{k_i}{c_{cost}}\times\frac{\sqrt[4]{d_{h,c_i}}+1}{|k_i|},$ 

где $k_i$ - множество домов, для которых пункт выдачи заказов $c_i$ является ближайшим, $d_{h,c} = \sqrt{(x_{h} - c_x)^2 + (y_{h} - c_y)^2}$ - Евклидово расстояние от дома $h$ в квартале $k$ до пункта выдачи заказов $c$ в этом же квартале, $C$ - ожидаемая прибыль от всех открытых ПВЗ, $c_{cost}$ - расходы на открытие одного ПВЗ.

Найдите координаты размещения ПВЗ, максимизирующие получаемую прибыль.
### Input Format:

В первой строке файла с открытыми данными задаются четыре числа $1 \leq k \leq 10^3$, $1 \leq n \leq 10^5$, $1 \leq c_{cost} \leq 10^3$, $1 \leq C \leq 10^4$, разделенные пробелами, где $k$ - число кварталов в районе, $n$ - общее число домов в районе, $c_{cost} \leq C$ - расходы на открытие одного ПВЗ, а $C$ - константа для вычисления дохода от открытия всех ПВЗ.

Далее следует $n$ строк c парами чисел $-10^9 \leq x_i, y_i \leq 10^9, 1 \leq i \leq k$, разделенных пробелами и задающих двумерные координаты каждого дома.

Ссылка на файл с входными данными: https://disk.yandex.ru/d/XNX_yGbysEvNLg

### Output Format:

Первая строка файла с ответом должна содержать одно число $C_{found}$ $-$ максимально достижимую прибыль, соответствующую найденным координатам центров выдачи заказов. На $2\times k$ последующих строках должны идти сначала $k$ пар чисел с плавающей точкой, разделенные запятыми $-$ координаты $x_i, y_i, 1 \leq i \leq k$ центров выдачи заказов, где $-2\times 10^9 \leq x_i, y_i \leq 2\times 10^9$, а затем должны идти $k$ строк с целыми числами, разделенными пробелами --- индексы домов $0 \leq i_{h} \leq n-1$, принадлежащих каждому ПВЗ, начиная с нуля.

Найденное значение $C_{found}$ должно соответствовать координатам точек и не должно быть меньше авторского.

## Example Test Cases

