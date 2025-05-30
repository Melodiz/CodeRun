# Solution for https://coderun.yandex.ru/problem/space-scavenger
# Other solutions: https://github.com/Melodiz/CodeRun

rules = {}
memo = {}

def count_moves(direction, parameter):
    if (direction, parameter) in memo:
        return memo[(direction, parameter)]

    if parameter == 1:
        return 1

    total_moves = 1  # Initial move
    rule_string = rules.get(direction, "")

    for char_in_rule in rule_string:
        total_moves += count_moves(char_in_rule, parameter - 1)
    
    memo[(direction, parameter)] = total_moves
    return total_moves

def main():
    global rules, memo
    rules = {}
    memo = {}
    
    directions_order = ['N', 'S', 'W', 'E', 'U', 'D']
    for i in range(6):
        rules[directions_order[i]] = input()
    
    command_line = input().split()
    initial_direction = command_line[0]
    initial_parameter = int(command_line[1])
    
    result = count_moves(initial_direction, initial_parameter)
    print(result)

if __name__ == "__main__":
    main()
