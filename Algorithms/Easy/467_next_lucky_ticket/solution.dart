// Solution for https://coderun.yandex.ru/problem/next-lucky-ticket
// Other solutions: https://github.com/Melodiz/CodeRun

import 'dart:io';

bool isLucky(int k) {
  String numStr = k.toString();
  int firstSum = 0;
  int secondSum = 0;
  
  for (int i = 0; i < 3; i++) {
    firstSum += int.parse(numStr[i]);
    secondSum += int.parse(numStr[i + 3]);
  }
  
  return firstSum == secondSum;
}

void main() {
  int n = int.parse(stdin.readLineSync()!);
  
  for (int k = n + 1; k < 1000000; k++) {
    if (isLucky(k)) {
      print(k);
      break;
    }
  }
}
