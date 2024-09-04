def get_all_misprints_for_fixes(a, b):
    alphabet = set(a) | set(b)
    typos_a = set()
    typos_b = set()
    
    # Generate all possible misprints for a
    for i in range(len(a)):
        # Deletion
        typos_a.add(a[:i] + a[i+1:])
        # Substitution
        for char in alphabet:
            typos_a.add(a[:i] + char + a[i+1:])
        # Insertion
        for char in alphabet:
            typos_a.add(a[:i] + char + a[i:])
    # Transposition
    for i in range(len(a) - 1):
        typos_a.add(a[:i] + a[i+1] + a[i] + a[i+2:])

    typos_a.add(a[1:])
    typos_a.add(a[:-1])
    for char in alphabet:
        typos_a.add(a + char)
        typos_a.add(char + a)
        typos_a.add(a[:-1]+char)
        typos_a.add(char+a[1:])
    
    # Generate all possible misprints for b
    for i in range(len(b)):
        # Deletion
        typos_b.add(b[:i] + b[i+1:])
        # Substitution
        for char in alphabet:
            typos_b.add(b[:i] + char + b[i+1:])
        # Insertion
        for char in alphabet:
            typos_b.add(b[:i] + char + b[i:])
    # Transposition
    for i in range(len(b) - 1):
        typos_b.add(b[:i] + b[i+1] + b[i] + b[i+2:])
    typos_b.add(b[1:])
    typos_b.add(b[:-1])
    for char in alphabet:
        typos_b.add(b + char)
        typos_b.add(char + b)
        typos_b.add(b[:-1]+char)
        typos_b.add(char+b[1:])

    intesect = typos_a.intersection(typos_b)
    if len(intesect) == 0: return f'{a} {b} Error'
    else: return f'{a} 2 {intesect.pop()} {b}'


def read():
    data = []
    with open('result.txt', 'r') as file:
        for line in file.readlines():
            data.append(line.strip())
    return data

def main():
    data = read()
    result = []
    for line in data:
        if line[-5:] == 'Error':
            result.append(get_all_misprints_for_fixes(*line[:-6].split(' ')))
        else:
            result.append(line)
    with open('result_corrected.txt', 'w') as file:
        for line in result:
            file.write(line + '\n')

if __name__ == '__main__':
    main()

