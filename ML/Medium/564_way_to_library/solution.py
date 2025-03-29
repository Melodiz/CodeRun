import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import gc  # Import garbage collection module

def load_data():
    books = []
    queries = []
    for _ in range(int(input())):
        books.append(input().strip())
    for _ in range(int(input())):
        queries.append(input().strip())
    return books, queries

def find_similar_books_batch(query_vecs, nbrs, book_titles):
    distances, indices = nbrs.kneighbors(query_vecs)
    similar_books_batch = [[book_titles[idx] for idx in indices[i]] for i in range(len(indices))]
    return similar_books_batch

def main():
    # Load data
    book_titles, queries = load_data()

    # Convert book titles to vector representations using TF-IDF
    vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(2, 3), strip_accents='unicode', max_features=10000)
    X = vectorizer.fit_transform(book_titles).astype(np.float32)  # Use float32 to reduce memory usage

    # Train NearestNeighbors model
    nbrs = NearestNeighbors(n_neighbors=3, algorithm='auto', metric='cosine').fit(X)

    # Process queries in batches
    batch_size = 100  # Adjust batch size as needed
    for start in range(0, len(queries), batch_size):
        end = min(start + batch_size, len(queries))
        query_vecs = vectorizer.transform(queries[start:end]).astype(np.float32)  # Use float32 to reduce memory usage

        # Find similar books for the current batch of queries
        similar_books_batch = find_similar_books_batch(query_vecs, nbrs, book_titles)

        # Free up memory by deleting large objects and calling garbage collector
        del query_vecs
        gc.collect()

        # Evaluate the model for the current batch
        for i in range(end - start):
            # print top-3 similar books for each query
            print(3)
            for j in range(3):
                print(similar_books_batch[i][j])

if __name__ == "__main__":
    main()