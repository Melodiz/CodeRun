# Solution for https://coderun.yandex.ru/problem/krosh-and-string
# Other solutions: https://github.com/Melodiz/CodeRun

import 'dart:io';

void main() {
  var reader = stdin;

  int n = int.parse(reader.readLineSync()!);
  String s = reader.readLineSync()!;

  List<String> stack = [];

  for (int i = 0; i < s.length; i++) {
    String char = s[i];
    
    if (stack.isNotEmpty && stack.last == char) {
      stack.removeLast();
    } else {
      stack.add(char);
    }
  }

  if (stack.isEmpty) {
    stdout.writeln(1);
  } else {
    stdout.writeln(0);
  }
}