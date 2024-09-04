import re
import sys


def single_word(word, set_of_words):
    alphabet = sorted(set('абвгдеёжзийклмнопрстуфхцчшщъыьэюяc'))

    def generate_words_with_typos(word_to_create):
        typos = set()
        for char in alphabet:
            typos.add(word_to_create + char)
            typos.add(char + word_to_create)
        # Single character typos
        for i in range(len(word_to_create)):
            # Deletion
            typos.add(word_to_create[:i] + word_to_create[i+1:])
            for char in alphabet:
                # Substitution
                typos.add(word_to_create[:i] + char + word_to_create[i+1:])
                # Insertion
                typos.add(word_to_create[:i] + char + word_to_create[i:])
            if i < len(word_to_create) - 1:
                # Swap
                typos.add(word_to_create[:i] + word_to_create[i+1] +
                          word_to_create[i] + word_to_create[i+2:])

        return typos
    
    if word in set_of_words:
        return word
    word_typos = generate_words_with_typos(word)
    for typo in word_typos:
        if typo in set_of_words:
            return typo
    return "404"


def check_words_with_typos(word, set_of_words):
    alphabet = sorted(set('абвгдеёжзийклмнопрстуфхцчшщъыьэюяc'))

    def generate_words_with_typos(word_to_create):
        typos = set()
        for char in alphabet:
            typos.add(word_to_create + char)
            typos.add(char + word_to_create)
        # Single character typos
        for i in range(len(word_to_create)):
            # Deletion
            typos.add(word_to_create[:i] + word_to_create[i+1:])
            for char in alphabet:
                # Substitution
                typos.add(word_to_create[:i] + char + word_to_create[i+1:])
                # Insertion
                typos.add(word_to_create[:i] + char + word_to_create[i:])
            if i < len(word_to_create) - 1:
                # Swap
                typos.add(word_to_create[:i] + word_to_create[i+1] +
                          word_to_create[i] + word_to_create[i+2:])

        return typos

    if word in set_of_words:
        return f'{word} 0'

    # Check with one typo
    typos = generate_words_with_typos(word)
    intersection_level_1 = set_of_words.intersection(typos)
    if intersection_level_1:
        return f'{word} 1 {intersection_level_1.pop()}'

    # check with two typos
    words_typos = set()
    for word_from_dict in set_of_words:
        words_typos.update(generate_words_with_typos(word_from_dict))
    mid = words_typos.intersection(typos)

    if mid:
        new_word = mid.pop()
        return f'{word} 2 {new_word} ' + single_word(new_word, set_of_words)

    return word + "404"


def read_words(file_path='dict.txt'):
    result = set()
    for line in open(file_path, 'r').readlines():
        result.add(line.strip())
    return result


def read_queries(file_path='queries.txt'):
    result = []
    for line in open(file_path, 'r').readlines():
        result.append(line.strip())
    return result


def get_data():
    words = read_words()
    queries = read_queries()
    return words, queries


def save_result(result, file_path='result.txt'):
    with open(file_path, 'w') as f:
        for word in result:
            f.write(f'{word}\n')
    print(f'Result saved to {file_path}')


def test():
    dict = {'яхта', 'метро', 'такси'}
    queries = ['яхты', 'емтто', 'такси', 'автобус']
    for query in queries:
        print(check_words_with_typos(query, dict))


def read_test_result(file_path='result_test.txt'):
    data = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data


if __name__ == '__main__':
    test()
