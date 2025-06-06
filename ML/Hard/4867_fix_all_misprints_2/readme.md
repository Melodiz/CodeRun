# [Исправить все опечатки (2.0)](link)

## Description


Рассмотрим несколько самых популярных ошибок при вводе информации:

* Случайно пропущена буква. Слово «метро» может быть введено «мтро».
* Случайно две соседние буквы перепутаны местами. Слово «метро» может быть введено «емтро».
* Случайно добавлена лишняя буква. Слово «метро» может быть введено «метрор».
 

Вам необходимо скачать архив, в котором находится два файла:

* dict.txt – набор слов, которые мы будем считать корректными в данной задаче. Обратите внимание, что в него входят не все слова русского языка.
* queries.txt – набор из 100.000 слов для обработки. Для каждого слова из данного набора следует определить, можно ли, исправив несколько опечаток, получить слово из словаря.


### Input Format:

``dict.txt`` (в примере всего три слова в словаре)

Ссылка на файл: https://disk.yandex.ru/d/01cRNfnvEWn-Tg


```
яхта
метро
такси
```

``queries.txt`` (в примере всего четыре слова для обработки)

Ссылка на файл: 

https://disk.yandex.ru/d/0YJT6qGyZXlfFA


```
яхты
емтто
такси
автобус
```
 
Для каждого слова сформируйте строку в одном из следующих форматов:

* «слово» 0 – «слово» есть в словаре, т.е. написано без ошибок;
* «слово 1 исправление» $-$ одну ошибку можно исправить в «слово» и получить «исправление», которое есть в словаре;
* «слово 2 исправление1 исправление2» $-$ одну ошибку можно исправить в «слово» и получить «исправление1», затем в «исправление1» можно исправить еще одну ошибку и получить «исправление2», которое есть в словаре. Ошибки могут быть разного типа.
* «слово 3 исправление1 исправление2 исправление3» $-$ аналогично предыдущему
* «слово 4 исправление1 исправление2 исправление3 исправление4» $-$ аналогично предыдущему
* «слово 5+» -- необходимо сделать не менее пяти исправлений, чтобы получить какое-то слово из словаря.

### Output Format:

``answer.txt`` (пример файла-ответа, может быть любое имя)

```
яхты 2 яхт яхта
емтто 3 метто мето метро
такси 0
автобус 5+
```

Вы должны отправить файл с 100.000 строками. 
Слова нужно обрабатывать в том порядке, как они идут в файле 
``queries.txt``. Кодировка вашего файла должна быть ``UTF-8``.

Решение будет зачтено, если в результирующем файле не менее ``99%`` корректных строк.

## Example Test Cases

