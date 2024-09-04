from pyxdameraulevenshtein import damerau_levenshtein_distance_seqs
from utils import read_words, read_test_result, save_result, read_queries
from tqdm import tqdm
from joblib import Parallel, delayed


def get_all_misprints(a, b):
    alphabet = set(a) | set(b)
    typos_a = set()
    typos_b = set()

    # Generate all possible misprints for a
    for i in range(len(a)):
        # Deletion
        typos_a.add(a[:i] + a[i+1:])
        # Substitution
        for char in alphabet:
            typos_a.add(a[:i] + char + a[i+1:])
        # Insertion
        for char in alphabet:
            typos_a.add(a[:i] + char + a[i:])
    # Transposition
    for i in range(len(a) - 1):
        typos_a.add(a[:i] + a[i+1] + a[i] + a[i+2:])

    typos_a.add(a[1:])
    typos_a.add(a[:-1])
    for char in alphabet:
        typos_a.add(a + char)
        typos_a.add(char + a)
        typos_a.add(a[:-1]+char)
        typos_a.add(char+a[1:])

    # Generate all possible misprints for b
    for i in range(len(b)):
        # Deletion
        typos_b.add(b[:i] + b[i+1:])
        # Substitution
        for char in alphabet:
            typos_b.add(b[:i] + char + b[i+1:])
        # Insertion
        for char in alphabet:
            typos_b.add(b[:i] + char + b[i:])
    # Transposition
    for i in range(len(b) - 1):
        typos_b.add(b[:i] + b[i+1] + b[i] + b[i+2:])
    typos_b.add(b[1:])
    typos_b.add(b[:-1])
    for char in alphabet:
        typos_b.add(b + char)
        typos_b.add(char + b)
        typos_b.add(b[:-1]+char)
        typos_b.add(char+b[1:])

    intesect = typos_a.intersection(typos_b)
    if len(intesect) == 0:
        return f'{a} {b} Error'
    else:
        return f'{a} 2 {intesect.pop()} {b}'


def process_query_brute(query, words_list):
    n = len(query)
    set_query = set(query)
    relevant_words = []
    for word in words_list:
        if abs(len(word) - n) > 2:
            continue
        if len(set_query.symmetric_difference(set(word))) > 2:
            continue
        relevant_words.append(word)
    indeses = damerau_levenshtein_distance_seqs(query, relevant_words)
    if len(indeses) == 0:
        return f'{query} 3+'
    min_value = min(indeses)
    if min_value > 2:
        return f'{query} 3+'

    closest_word = ''
    for i in range(len(indeses)):
        if indeses[i] == min_value:
            closest_word = relevant_words[i]
            break

    if min_value == 1:
        return f'{query} 1 {closest_word}'
    elif min_value == 2:
        return get_all_misprints(query, closest_word)
    elif min_value == 0:
        return f'{query} 0'


def process_query_lite(query, words_list):
    n = len(query)
    indeses = damerau_levenshtein_distance_seqs(query, words_list)
    if len(indeses) == 0:
        return '404'
    min_value = min(indeses)
    if min_value > 2:
        return '404'
    closest_word = ''
    for i in range(len(indeses)):
        if indeses[i] == min_value:
            closest_word = words_list[i]
            break
    if min_value == 1:
        return f'{query} 1 {closest_word}'
    elif min_value == 2:
        return get_all_misprints(query, closest_word)


def main():
    words = read_words()
    queries = read_queries()
    print(len(words), len(queries))
    results = []
    for query in tqdm(queries[:1000], desc='Searching for closest words'):
        results.append(process_query_brute(query, words))
    save_result(results, 'result.txt')


if __name__ == '__main__':
    main()
