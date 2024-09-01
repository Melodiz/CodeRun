from collections import Counter
import sys
def most_frequent_word(text):
    word_count = Counter(text)
    max_value = max(word_count.values())
    most_common_words = [word for word, count in word_count.items() if count == max_value]
    return sorted(most_common_words)[0]


def main():
    # Read the input lines there are 
    text = []
    for line in sys.stdin.readlines():
        text += line.strip().split()
        
    print(most_frequent_word(text))


if __name__ == "__main__":
    main()