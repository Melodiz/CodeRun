# Трёхбуквенная баллада

Выкладывание поля для сапера оказалось неожиданно приятной задачей – ты словно медитировал, укладывая плитки на поле. И в процессе тебя осенило: пока Кодеруна нет, кто-то должен заботиться о цифровом мире. Почему бы не быть этим кем-то? Ты благодаришь странного человека с рюкзаком, спешишь дальше – и тут же видишь персонажа в беде.

На высоком подоконнике сидит придворный менестрель. Он сгорбился и утирает слёзы. – Моё вдохновение – его как будто кто-то украл... – всхлипывает менестрель.

– Я должен сочинить балладу в честь Принцессы Брейс, но всё, что у меня выходит – это бессмысленные нагромождения букв и пафоса. Мне нужно нечто простое, ясное... Идеальное! Только палиндромы достойны её ушей!

– Три буквы, читающиеся одинаково вперёд и назад. Вот и всё, что я прошу... Только три... – он простирает тебе свиток с черновиком и умоляюще смотрит в глаза.

### Формат ввода

В качестве аргументов вашей функции передаются 2 параметра:

* `ballad` - текст баллады. Длина баллады не превышает `3 * 10^5`. Гарантируется, что баллада может содержать только строчные буквы английского алфавита и пробелы. Также гарантируется, что баллада не пуста. Баллада не может начинаться с пробела или заканчиваться им.

* `Натуральное число n` - длина баллады.

### Формат вывода

В качестве ответа ваша программа должна вернуть одно число `x` – количество способов вычеркнуть из баллады все пробелы и некоторые буквы таким образом, чтобы осталось три буквы, которые образуют палиндром. Палиндромом называется строка, которая читается одинаково слева-направо и справа-налево. Два способа вычеркивания считаются различными, если найдется хотя бы один индекс, такой, что в первом способе буква с таким индексом в предложении вычеркнута, а во втором – нет.

### Ограничения

* Ограничение времени: 2 с
* Ограничение памяти: 256 МБ

### Пример 1

Ввод:
`treasure`

Вывод:
`8`

### Пример 2

Ввод:
`you will never find the treasure`

Вывод:
`146`

---

# Three-Letter Ballad

Laying out a field for a sapper turned out to be an unexpectedly pleasant task – you were meditating, laying tiles on the field. And in the process, it dawned on you: while Coderun isn't around, someone has to take care of the digital world. Why not be that someone? You thank a strange person with a backpack, rush further – and there you see a character in distress.

On a high windowsill sits the court minstrel. He hunches over and wipes his tears. – My inspiration – it's as if someone stole it... – whimpers the minstrel.

– I must compose a ballad in honor of Princess Brace, but all that comes out is meaningless piles of letters and pathos. I need something simple, clear... Ideal! Only palindromes are worthy of her ears!

– Three letters, reading the same forwards and backward. That's all I ask... Just three... – he hands you a scroll with a draft and looks at you imploringly.

### Input Format

Your function arguments will receive 2 parameters:

* `ballad` - the text of the ballad. The length of the ballad does not exceed `3 * 10^5`. It is guaranteed that the ballad can only contain lowercase English letters and spaces. It is also guaranteed that the ballad is not empty. The ballad cannot start or end with a space.

* `Natural number n` - the length of the ballad.

### Output Format

Your program should return a single number `x` – the number of ways to erase all spaces and some letters from the ballad such that three letters remain, forming a palindrome. A palindrome is a string that reads the same forwards and backward. Two ways of erasing are considered different if there is at least one index such that in the first way the letter at that index in the sentence is erased, and in the second way – it is not.

### Constraints

* Time limit: 2 s
* Memory limit: 256 MB

### Example 1

Input:
`treasure`

Output:
`8`

### Example 2

Input:
`you will never find the treasure`

Output:
`146`