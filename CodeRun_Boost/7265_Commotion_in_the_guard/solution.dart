List<int> solve(int n, int m, List<int> swaps) {
  List<int> positions = List<int>.generate(2 * n, (index) => index + 1);

  int methodsOnLeftCount = n;

  List<int> result = List.filled(m, 0);

  for (int i = 0; i < m; i++) {
    int p1Orig = swaps[2 * i];
    int p2Orig = swaps[2 * i + 1];

    int p1Idx = p1Orig - 1;
    int p2Idx = p2Orig - 1;

    bool p1IsLeft = (p1Idx < n);
    bool p2IsLeft = (p2Idx < n);

    if (p1IsLeft != p2IsLeft) {
      int guard1 = positions[p1Idx];
      int guard2 = positions[p2Idx];

      bool guard1IsMethod = (guard1 <= n);
      bool guard2IsMethod = (guard2 <= n);

      if (p1IsLeft) {
        if (guard1IsMethod) {
          methodsOnLeftCount--;
        }
        if (guard2IsMethod) {
          methodsOnLeftCount++;
        }
      } else {
        if (guard2IsMethod) {
          methodsOnLeftCount--;
        }
        if (guard1IsMethod) {
          methodsOnLeftCount++;
        }
      }
    }

    int temp = positions[p1Idx];
    positions[p1Idx] = positions[p2Idx];
    positions[p2Idx] = temp;

    result[i] = methodsOnLeftCount;
  }

  return result;
}