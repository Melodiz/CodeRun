# Solution for https://coderun.yandex.ru/problem/cha_cha
# Other solutions: https://github.com/Melodiz/CodeRun

import math

def calculate_final_grade(grades_str):
    numeric_grades = []
    for grade_char in grades_str:
        numeric_grades.append(ord('A') - ord(grade_char) + 25)

    average_numeric_grade = sum(numeric_grades) / len(numeric_grades)

    rounded_grade = math.floor(average_numeric_grade + 0.5)

    min_numeric_grade = min(numeric_grades)

    max_allowed_grade = min(25, min_numeric_grade + 1) 
    
    final_numeric_grade = min(rounded_grade, max_allowed_grade)
    
    final_grade_char = chr(ord('A') + (25 - int(final_numeric_grade)))
    
    return final_grade_char

def main():
    s = input()
    result = calculate_final_grade(s)
    print(result)

if __name__ == "__main__":
    main()
