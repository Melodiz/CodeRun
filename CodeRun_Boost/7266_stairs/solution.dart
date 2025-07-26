import 'dart:math';

List<int> solve(int n, List<int> a) {
  var result = List<int>.filled(n + 1, 0, growable: false);
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    result[0] = 1;
    result[1] = a[0];
    return result;
  }

  final intMax = 9007199254740991; // JS Number.MAX_SAFE_INTEGER

  var dpPlus = List<int>.filled(n, 0, growable: false);
  var dpMinus = List<int>.filled(n, 0, growable: false);
  dpPlus[0] = a[0];
  dpMinus[0] = -a[0];

  for (var i = 1; i < n; ++i) {
    var currentPlus = a[i];
    var currentMinus = -a[i];
    var plusOk = false;
    var minusOk = false;

    if (dpPlus[i - 1] != intMax && dpPlus[i - 1] <= currentPlus) plusOk = true;
    if (dpMinus[i - 1] != intMax && dpMinus[i - 1] <= currentPlus) plusOk = true;

    if (dpPlus[i - 1] != intMax && dpPlus[i - 1] <= currentMinus) minusOk = true;
    if (dpMinus[i - 1] != intMax && dpMinus[i - 1] <= currentMinus) minusOk = true;

    if (!plusOk && !minusOk) {
      return List<int>.filled(n + 1, 0, growable: false);
    }
    
    dpPlus[i] = plusOk ? currentPlus : intMax;
    dpMinus[i] = minusOk ? currentMinus : intMax;
  }

  result[0] = 1;
  int current;

  if (dpPlus[n - 1] != intMax && dpMinus[n - 1] != intMax) {
      current = min(dpPlus[n - 1], dpMinus[n - 1]);
  } else if (dpPlus[n - 1] != intMax) {
      current = dpPlus[n - 1];
  } else {
      current = dpMinus[n-1];
  }
  result[n] = current;

  for (var i = n - 2; i >= 0; --i) {
      int prevPlus = dpPlus[i];
      int prevMinus = dpMinus[i];

      if (prevPlus != intMax && prevPlus <= current) {
          if (prevMinus != intMax && prevMinus <= current) {
              current = min(prevPlus, prevMinus);
          } else {
              current = prevPlus;
          }
      } else if (prevMinus != intMax && prevMinus <= current) {
          current = prevMinus;
      }
      result[i+1] = current;
  }

  return result;
}