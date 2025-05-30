# Solution for https://coderun.yandex.ru/problem/unique-users
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    n = int(input())
    users = set()
    for _ in range(n):
        row = input()
        name, domain = row.split('@')
        name = name.split('-')[0].replace('.', '')
        domain = domain.split('.')[:-1]
        users.add(f"{name}@{'.'.join(domain)}")
    print(len(users))

if __name__ == "__main__":
    main()
