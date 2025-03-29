def create_all(list_of_words, aplphabet):
    result = set()
    for word in list_of_words:
        result.update(all_typos(word, aplphabet))
    return result


def save_to_file(result):
    with open('result.txt', 'w') as f:
        for word in result:
            f.write(f'{word}\n')
    print(f'Result saved to result.txt')

def all_typos(word, alphabet):
    # return the set of all possible typos for the given word:
    # 1. deletion (deleting one character from the word including the start and end)
    # 2. substitution (changing one character in the word)
    # 3. insertion (adding one character to the word, even at the start and end)
    # 4. transposition (swapping two adjacent characters)
    result = set()
    # deletion
    for i in range(len(word)):
        result.add(word[:i] + word[i+1:])
        # substitution & insertion
        for char in alphabet:
            result.add(word[:i] + char + word[i+1:])
            result.add(word[:i] + char + word[i:])
    for char in alphabet:
        result.add(word + char)
    # transposition
    for i in range(len(word) - 1):
        result.add(word[:i] + word[i+1] + word[i] + word[i+2:])
    return result


def find_lite(word, set_closest_words, aplphabet):
    if word in set_closest_words:
        return f'{word} 0'
    l1_query = create_all([word], aplphabet)
    for l1_word in l1_query:
        if l1_word in set_closest_words:
            return f'{word} 1 {l1_word}'
    l1_words = create_all(set_closest_words, aplphabet)
    # check if there is a word in the l1_words which is also in l1_query and return if not
    common = l1_words.intersection(l1_query)
    if len(common) == 0:
        return f'{word} 3+'
    else:
        mid_word = common.pop()
        return f'{word} 2 {mid_word} {find_mid(mid_word, set_closest_words, aplphabet)}'


def find_mid(mid_word, l0_words, alphabet):
    l1_mid_word = create_all([mid_word], alphabet)
    for typo in l1_mid_word:
        if typo in l0_words:
            return typo
    return '404'


def find_brute(query, set_of_words, aplphabet):
    if query in set_of_words:
        return f'{query} 0'
    l1_query = create_all([query], aplphabet)
    for l1_word in l1_query:
        if l1_word in set_of_words:
            return f'{query} 1 {l1_word}'
    for l1_word in l1_query:
        l2_words = create_all([l1_word], aplphabet)
        for l2_word in l2_words:
            if l2_word in set_of_words:
                return f'{query} 2 {l1_word} {l2_word}'
    return f'{query} 3+'


def test_typos():
    word = 'hello'
    alphabet = set('abc')
    deletions = {'ello', 'hllo', 'helo', 'hell'}
    insertions = {
        'ahello', 'bhello', 'chello',  # insertions at start
        'haello', 'hbello', 'hcello',  # insertions after first character
        'heallo', 'hebllo', 'hecllo',  # insertions after second character
        'helalo', 'helblo', 'helclo',  # insertions after third character
        'hellao', 'hellbo', 'hellco',  # insertions after fourth character
        'helloa', 'hellob', 'helloc'  # insertions at end
    }
    substitutions = {
        'aello', 'bello', 'cello',  # substitutions for first character
        'hallo', 'hbllo', 'hcllo',  # substitutions for second character
        'healo', 'heblo', 'heclo',  # substitutions for third character
        'helao', 'helbo', 'helco',  # substitutions for fourth character
        'hella', 'hellb', 'hellc'  # substitutions for fifth character
    }
    transpositions = {
        'ehllo', 'hlelo', 'hello', 'helol'}
    expected_typos = deletions.union(insertions, substitutions, transpositions)
    typos = create_all([word], alphabet)
    assert typos == expected_typos, f'Expected {expected_typos}, got {typos}'
    print('Typos generated correctly')


def test_words():
    set_closest_words = {'яхта', 'метро', 'такси'}
    queries = ['яхты', 'емтто', 'такси', 'автобус']
    alph = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    assert find_lite('яхты', set_closest_words, alph) == 'яхты 1 яхта'
    assert find_lite('емтто', set_closest_words, alph) == 'емтто 2 емтро метро' or find_lite(
        'емтто', set_closest_words, alph) == 'емтто 2 метто метро'
    assert find_lite('такси', set_closest_words, alph) == 'такси 0'
    assert find_lite('автобус', set_closest_words, alph) == 'автобус 3+'

    assert find_brute('яхты', set_closest_words, alph) == 'яхты 1 яхта'
    assert find_brute('емтто', set_closest_words, alph) == 'емтто 2 емтро метро' or find_brute(
        'емтто', set_closest_words, alph) == 'емтто 2 метто метро'
    assert find_brute('такси', set_closest_words, alph) == 'такси 0'
    assert find_brute('автобус', set_closest_words, alph) == 'автобус 3+'

    print("Test set passed")


def get_data():
    set_of_all_words = set()
    list_of_all_queries = []
    with open('dict.txt', 'r', encoding='utf-8') as file:
        for line in file:
            set_of_all_words.add(line.strip())
    with open('queries.txt', 'r', encoding='utf-8') as file:
        for line in file:
            list_of_all_queries.append(line.strip())
    alphabet = {'л', 'ж', 'в', 'ь', 'ю', 'э', 'о', 'т', 'м', 'а', 'я', 'щ', 'с', 'д', 'п', 'з', 'ц',
                'ш', 'е', 'c', 'ъ', 'ф', 'б', 'г', 'й', 'ч', 'ы', ' ', 'р', 'у', 'и', 'н', 'х', 'к'}
    return set_of_all_words, list_of_all_queries, alphabet


if __name__ == '__main__':
    test_typos()
    test_words()
