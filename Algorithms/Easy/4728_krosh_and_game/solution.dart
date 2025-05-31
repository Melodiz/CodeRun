import 'dart:io';

void main() {
  solve();
}

void solve() {
  const int MAX_N = 100000;
  List<bool> dp = List<bool>.filled(MAX_N + 1, false);

  // Precompute perfect squares up to MAX_N
  List<int> perfectSquares = [];
  int i = 1;
  while (i * i <= MAX_N) {
    perfectSquares.add(i * i);
    i++;
  }

  for (int j = 1; j <= MAX_N; j++) {
    bool canWinFromJ = false;
    for (int square in perfectSquares) {
      if (j - square >= 0) {
        if (!dp[j - square]) {
          canWinFromJ = true;
          break;
        }
      } else {
        break;
      }
    }
    dp[j] = canWinFromJ;
  }

  int q = int.parse(stdin.readLineSync()!);
  List<String> results = [];
  for (int k = 0; k < q; k++) {
    int n = int.parse(stdin.readLineSync()!);
    results.add(dp[n] ? "1" : "0");
  }

  stdout.write(results.join("\n"));
}