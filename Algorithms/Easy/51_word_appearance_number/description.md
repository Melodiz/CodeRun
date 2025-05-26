# [Номер появления слова](link)

## Description

Во входном файле (вы можете читать данные из файла input.txt)
записан текст. Словом считается последовательность непробельных символов
идущих подряд, слова разделены одним или большим числом пробелов
или символами конца строки.
Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось 
в этом тексте ранее.
### Input Format:

Вводится текст.

### Output Format:

Выведите ответ на задачу.

## Example Test Cases

### Example 1

**Input:**
```
one two one tho three


```

**Output:**
```
0 0 1 0 0 

```

### Example 2

**Input:**
```
She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.


```

**Output:**
```
0 0 0 0 0 0 1 0 0 1 0 0 1 0 2 2 0 0 0 0 1 2 3 3 1 1 4 0 1 0 1 2 4 1 5 0 0 

```

### Example 3

**Input:**
```
aba aba; aba @?"

```

**Output:**
```
0 0 1 0 

```

