import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
# import time

def load_data():
    books = []
    queries = []
    correct_responses = []
    with open('ML/Medium/564_way-to-library/htgtl books.txt', 'r') as file:
        for line in file.readlines():
            books.append(line.strip())
    with open('ML/Medium/564_way-to-library/htgtl simple public queries.txt', 'r') as file:
        arr = file.readlines()
        for i in range(0, len(arr), 2):
            queries.append(arr[i].strip())
            correct_responses.append(arr[i+1].strip())
    return books, queries, correct_responses

def find_similar_books_batch(query_vecs, nbrs, book_titles):
    distances, indices = nbrs.kneighbors(query_vecs)
    similar_books_batch = [[book_titles[idx] for idx in indices[i]] for i in range(len(indices))]
    return similar_books_batch

def main():
    # Load data
    book_titles, queries, correct_responses = load_data()
    # start_time = time.time() 

    # Convert book titles to vector representations using TF-IDF
    vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(2, 3), strip_accents='unicode')
    X = vectorizer.fit_transform(book_titles)

    # Train NearestNeighbors model
    nbrs = NearestNeighbors(n_neighbors=3, algorithm='auto', metric='cosine').fit(X)

    # Vectorize all queries at once
    query_vecs = vectorizer.transform(queries)

    # Find similar books for all queries
    similar_books_batch = find_similar_books_batch(query_vecs, nbrs, book_titles)

    # Evaluate the model
    counter = 0
    for i in range(len(queries)):
        if similar_books_batch[i][0] == correct_responses[i]:
            counter += 1

    # end_time = time.time()
    print(f'Accuracy: {counter}/{len(queries)}')
    # print(f'Time taken: {end_time - start_time:.2f} seconds')

if __name__ == "__main__":
    main()