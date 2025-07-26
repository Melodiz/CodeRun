import 'dart:math';

int solve(int n, List<int> a) {
  a.sort();

  int left = 0;
  int maxKeep = 0;

  for (int right = 0; right < n; right++) {
    while (a[right] - a[left] >= n) {
      left++;
    }

    int currentKeep = right - left + 1;

    if (currentKeep > maxKeep) {
      maxKeep = currentKeep;
    }
  }

  int minMoves = n - maxKeep;

  return minMoves;
}