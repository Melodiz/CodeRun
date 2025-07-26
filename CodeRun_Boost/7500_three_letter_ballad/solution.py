def solve(ballad: str, n: int) -> int:
    letters = [char for char in ballad if char.isalpha()]
    m = len(letters)

    if m < 3:
        return 0

    left_counts = [0] * 26
    right_counts = [0] * 26

    left_counts[ord(letters[0]) - 97] += 1

    for i in range(2, m):
        right_counts[ord(letters[i]) - 97] += 1

    total_palindromes = 0

    for j in range(1, m - 1):
        current_contribution = 0
        for i in range(26):
            current_contribution += left_counts[i] * right_counts[i]
        
        total_palindromes += current_contribution

        left_counts[ord(letters[j]) - 97] += 1
        
        if j + 1 < m:
            right_counts[ord(letters[j + 1]) - 97] -= 1

    return total_palindromes