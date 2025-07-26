#include <string>
#include <vector>

long long solve(const std::string& ballad, int n) {
    long long total_ways = 0;

    // suffix_char_counts[i][char_code] stores the count of 'a' + char_code
    // in ballad[i...n-1]
    // This is essentially precomputing all 'right_counts' for every possible starting point.
    std::vector<std::vector<int>> suffix_char_counts(n + 1, std::vector<int>(26, 0));

    for (int i = n - 1; i >= 0; --i) {
        suffix_char_counts[i] = suffix_char_counts[i + 1]; // Inherit counts from the suffix to the right
        if (ballad[i] != ' ') {
            suffix_char_counts[i][ballad[i] - 'a']++; // Add current character if not a space
        }
    }

    // left_counts[char_code] will store the count of 'a' + char_code
    // in ballad[0...j-1] as we iterate j
    std::vector<int> current_left_counts(26, 0);

    // Iterate through all possible indices for the middle character (c2)
    // j represents the index of c2. It must have at least one char before and one after.
    for (int j = 1; j < n - 1; ++j) { 
        // At the start of iteration for 'j', ballad[j-1] is the character that
        // is now on the left side of the potential middle character 'j'.
        if (ballad[j-1] != ' ') {
            current_left_counts[ballad[j-1] - 'a']++;
        }

        if (ballad[j] == ' ') {
            continue; // Middle character cannot be a space
        }

        // Now, current_left_counts contains counts for ballad[0...j-1].
        // suffix_char_counts[j+1] contains counts for ballad[j+1...n-1].
        
        // For each possible character 'a' through 'z' (which c1 and c3 can be)
        for (int char_code = 0; char_code < 26; ++char_code) {
            long long count_left = current_left_counts[char_code];
            long long count_right = suffix_char_counts[j + 1][char_code];
            
            total_ways += count_left * count_right;
        }
    }

    return total_ways;
}