#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool check(long long n, long long m, long long k) {
    return (k * k <= n + m) && ((k * k) / 2 <= (n < m ? n : m));
}

long long solution(long long n, long long m) {
    long long left = 0;
    long long right = 150000;

    long long ans = 0;

    while (left <= right) {
        long long mid = left + (right - left) / 2;

        if (check(n, m, mid)) {
            ans = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return ans;
}