# Исправить все опечатки

Problem ID: fix-all-misprints

URL: https://coderun.yandex.ru/problem/fix-all-misprints/

Tags: data structures, strings

Рассмотрим несколько самых популярных ошибок при вводе информации:

Случайно добавлена лишняя буква. Слово «метро» может быть введено «метрор».

Вам необходимо скачать архив, в котором находится два файла:

dictionary.txt (в примере всего три слова в словаре)

queries.txt (в примере всего четыре слова для обработки)

Для каждого слова сформируйте строку в одном из следующих форматов:

«слово 3+» -- необходимо сделать не менее трех исправлений, чтобы получить какое-то слово из словаря.

answer.txt (пример файла-ответа, может быть любое имя)

Вы должны отправить файл с 100.000 строками. 
Слова нужно обрабатывать в том порядке, как они идут в файле 
queries.txt. Кодировка вашего файла должна быть UTF-8.

Решение будет зачтено, если в результирующем файле не менее 99% корректных строк.

Скачать архив.

```
яхта
метро
такси
```

```
яхты
емтто
такси
автобус
```

```
яхты 1 яхта
емтто 2 метто метро
такси 0
автобус 3+
```

