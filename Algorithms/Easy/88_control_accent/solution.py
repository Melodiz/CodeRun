# Solution for https://coderun.yandex.ru/problem/control-accent
# Other solutions: https://github.com/Melodiz/CodeRun

def count_uppercase(word):
    return sum(1 for char in word if char.isupper())

def main():
    n = int(input())
    dictionary = {}
    for _ in range(n):
        dict_word = input().strip()
        lower_word = dict_word.lower()
        if lower_word not in dictionary:
            dictionary[lower_word] = set()
        dictionary[lower_word].add(dict_word)

    petya_text = input().split(' ')
    errors = 0

    for word in petya_text:
        lower_word = word.lower().strip()
        count_uppercase_in_word = count_uppercase(word)
        if lower_word not in dictionary:
            if count_uppercase_in_word != 1:
                errors += 1
        else:
            if word not in dictionary[lower_word]:
                errors += 1
            
    print(errors)

if __name__ == "__main__":
    main()