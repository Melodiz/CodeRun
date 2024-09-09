from utils import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from tqdm import tqdm
from joblib import Parallel, delayed


def process_query(query, set_of_all_words, vectorizer, nbrs, list_of_words, alphabet):
    if query in set_of_all_words:
        return f'{query} 0'
    _, indices = nbrs.kneighbors(vectorizer.transform([query]))
    closest_words = [list_of_words[index] for index in indices[0]]
    lite_result = find_lite(query, closest_words, alphabet)
    if '3+' in lite_result or '404' in lite_result:
        return find_brute(query, set_of_all_words, alphabet)
    else:
        return lite_result


def main():
    set_of_all_words, list_of_all_queries, alphabet = get_data()
    list_of_words = list(set_of_all_words)
    vectorizer = TfidfVectorizer(
        analyzer='char', ngram_range=(2, 3), strip_accents='unicode')
    X = vectorizer.fit_transform(list_of_words)
    nbrs = NearestNeighbors(n_neighbors=50, algorithm='auto', metric='cosine').fit(X)
    result = Parallel(n_jobs=-1)(delayed(process_query)(query, set_of_all_words, vectorizer, nbrs, list_of_words, alphabet) for query in tqdm(list_of_all_queries, desc='Searching for closest words'))
        
    save_to_file(result)


if __name__ == '__main__':
    main()
