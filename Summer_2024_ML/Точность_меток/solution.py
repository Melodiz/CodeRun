from math import gcd
from sklearn.metrics.cluster import contingency_matrix
import numpy as np
from sklearn.utils.validation import check_array, check_consistent_length
from sklearn.utils.multiclass import type_of_target
import warnings

def check_clusterings(labels_true, labels_pred):
    labels_true = check_array(
        labels_true,
        ensure_2d=False,
        ensure_min_samples=0,
        dtype=None,
    )

    labels_pred = check_array(
        labels_pred,
        ensure_2d=False,
        ensure_min_samples=0,
        dtype=None,
    )

    type_label = type_of_target(labels_true)
    type_pred = type_of_target(labels_pred)

    if "continuous" in (type_pred, type_label):
        msg = (
            "Clustering metrics expects discrete values but received"
            f" {type_label} values for label, and {type_pred} values "
            "for target"
        )
        warnings.warn(msg, UserWarning)

    # input checks
    if labels_true.ndim != 1:
        raise ValueError("labels_true must be 1D: shape is %r" % (labels_true.shape,))
    if labels_pred.ndim != 1:
        raise ValueError("labels_pred must be 1D: shape is %r" % (labels_pred.shape,))
    check_consistent_length(labels_true, labels_pred)

    return labels_true, labels_pred

def pair_confusion_matrix(labels_true, labels_pred):
    labels_true, labels_pred = check_clusterings(labels_true, labels_pred)
    n_samples = np.int64(labels_true.shape[0])

    # Computation using the contingency data
    contingency = contingency_matrix(
        labels_true, labels_pred, sparse=True
    )
    n_c = np.ravel(contingency.sum(axis=1))
    n_k = np.ravel(contingency.sum(axis=0))
    sum_squares = (contingency.data**2).sum()
    C = np.empty((2, 2), dtype=np.int64)
    C[1, 1] = sum_squares - n_samples
    C[0, 1] = contingency.dot(n_k).sum() - sum_squares
    C[1, 0] = contingency.transpose().dot(n_c).sum() - sum_squares
    C[0, 0] = n_samples**2 - C[0, 1] - C[1, 0] - sum_squares
    return C

def RandIndex(labels_true, labels_pred):
    contingency = pair_confusion_matrix(labels_true, labels_pred)
    numerator = contingency.diagonal().sum()
    denominator = contingency.sum()

    if numerator == denominator or denominator == 0:
        # Special limit cases: no clustering since the data is not split;
        # or trivial clustering where each document is assigned a unique
        # cluster. These are perfect matches hence return 1.0.
        return make_co_prime(1, 1)

    return make_co_prime(numerator, denominator)

def make_co_prime(numerator, denominator):
    g = gcd(numerator, denominator)
    return (numerator // g, denominator // g)


def RandIndex(labels_true, labels_pred):
    contingency = pair_confusion_matrix(labels_true, labels_pred)
    numerator = contingency.diagonal().sum()
    denominator = contingency.sum()

    if numerator == denominator or denominator == 0:
        # Special limit cases: no clustering since the data is not split;
        # or trivial clustering where each document is assigned a unique
        # cluster. These are perfect matches hence return 1.0.
        return make_co_prime(1, 1)

    return make_co_prime(numerator, denominator)


def make_co_prime(numerator, denominator):
    g = gcd(numerator, denominator)
    return (numerator // g, denominator // g)

def main():
    n = int(input())
    p = list(map(int, input().split()))
    v = list(map(int, input().split()))
    result = RandIndex(p, v)
    print(f'{result[0]}/{result[1]}')


if __name__ == '__main__':
    main()
    # test()
