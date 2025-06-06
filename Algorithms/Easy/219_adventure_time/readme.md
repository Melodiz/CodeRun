# [Время путешествий](link)

## Description

Путешественник Вася выбирает время для поездки в новую страну. Вася считает, что отпуск удался, если за время поездки температура в стране поднялась, причём чем сильнее она поднимется к отъезду относительно момента приезда, тем лучше.

Дан прогноз погоды на некоторый период вперёд, нужно указать изменение температуры за лучший для Васи период и лучшие даты (номера дней) приезда и отъезда. Если лучших вариантов несколько, то укажите номера дней самой короткой поездки с ближайшей датой окончания.
### Input Format:

В единственной строке записаны целые числа, разделённые пробелом $-$ ожидаемая температура в каждый из дней.

Количество дней не превыщает 10000, температура везде положительна и не превышает 45 градусов.


### Output Format:

3 числа, разделённые пробелом: изменение температуры за оптимальный период, номер дня приезда, номер дня отъезда (нумерация дней от 0). Гарантируется, что при оптимальном выборе поездки температура увеличится.

## Example Test Cases

### Example 1

**Input:**
```
3 4 1 6
```

**Output:**
```
5 2 3
```

