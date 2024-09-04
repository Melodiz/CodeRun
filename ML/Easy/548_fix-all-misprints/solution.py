import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from utils import *
from tqdm import tqdm
from joblib import Parallel, delayed
from bruteForceFind import process_query_brute, get_all_misprints, process_query_lite
from ErrorFixes import get_all_misprints_for_fixes, read


def process_query(query, vectorizer, nbrs, words_list):
    if query in words_list:
        return f'{query} 0'
    _, indices = nbrs.kneighbors(vectorizer.transform([query]))
    closest_words = [words_list[index] for index in indices[0]]
    lite_result = process_query_lite(query, closest_words)
    if lite_result != '404': 
        return lite_result
    else:
        full =  process_query_brute(query, words_list)
        if full[-5:] == 'Error': 
            return get_all_misprints_for_fixes(*full.split(' '))
        else:
            return full


def main():
    words_set = read_words()
    words_list = list(words_set)
    queries_list = read_queries()
    print("Data loading complete. Training...")

    vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(2, 3), strip_accents='unicode')
    X = vectorizer.fit_transform(words_list)
    nbrs = NearestNeighbors(n_neighbors=50, algorithm='auto', metric='cosine').fit(X)

    # Parallel processing of queries
    num_cores = -1  # Use all available cores
    results = Parallel(n_jobs=num_cores)(
        delayed(process_query)(query, vectorizer, nbrs, words_list) for query in tqdm(queries_list, desc='Searching for closest words')
    )
    # results = []
    # for query in tqdm(queries_list, desc='Searching for closest words'):
    #     results.append(process_query(query, vectorizer, nbrs, words_list))

    save_result(results, 'result.txt')

def fix_mistake_Nans():
    words_set = read_words()
    words_list = list(words_set)
    queries_list = read()
    print("Data loading complete. Training...")

    vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(2, 3), strip_accents='unicode')
    X = vectorizer.fit_transform(words_list)
    nbrs = NearestNeighbors(n_neighbors=50, algorithm='auto', metric='cosine').fit(X)

    result_fixed = []

    for query in tqdm(queries_list, desc='Searching for closest words'):
        if not query or query == "None" or query[0] == "N":
            result_fixed.append(process_query_brute(query, words_list))
        else:
            result_fixed.append(query)
    save_result(result_fixed, 'fixed_result.txt')

if __name__ == '__main__':
    main()
    fix_mistake_Nans()