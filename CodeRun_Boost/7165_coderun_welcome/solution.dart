import 'dart:math';

bool _check(int n, int m, int k) {
  return (k * k <= n + m) && ((k * k) ~/ 2 <= min(n, m));
}

int solve(int n, int m) {
  int left = 0;
  int right = 150000;
  int ans = 0;

  while (left <= right) {
    int mid = left + (right - left) ~/ 2;

    if (_check(n, m, mid)) {
      ans = mid;
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return ans;
}