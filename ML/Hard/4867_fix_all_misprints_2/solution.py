from tqdm import tqdm
def read_data():
    data = []
    with open('results.txt', 'r') as file:
        for line in file:
            data.append(parse(line.strip()))
    return data

def parse(sample):
    # "воспитаннясть: ('воспитанность', 1)" -> (воспитаннясть, воспитанность, 1)
    # "неоплатоэивк: ('неоплатоник', 2)" -> (неоплатоэивк, неоплатоник, 2)
    # Split by colon to get the misspelled word
    parts = sample.split(':')
    misspelled = parts[0].strip()
    if 'No' in sample: return (misspelled, None, 6)  # No distance for "No" samples
    # Extract the correct word and distance from the second part
    # First, find the content inside the parentheses
    inside_parentheses = parts[1].strip()
    # Extract the word (between quotes) and the number
    correct_word = inside_parentheses.split("'")[1]
    distance = int(inside_parentheses.split(',')[1].strip().rstrip(')'))
    
    return (misspelled, correct_word, distance)

def find_correction_path(word1, word2, max_dist):
    if max_dist > 4: return f'{word1} 5+'
    if word1 == word2:
        return f"{word1} 0"
    
    from collections import deque
    
    queue = deque()
    queue.append((word1, [word1], max_dist))
    visited = set([word1])
    
    while queue:
        current, path, remaining = queue.popleft()
        
        if current == word2:
            ans = f"{word1} {max_dist} {' '.join(path[1:])}"
            return ans
        if remaining == 0:
            continue
        
        length = len(current)
        # Generate neighbors (all possible 1-step corrections)
        neighbors = set()
        
        # Deletions
        for i in range(length):
            new_word = current[:i] + current[i+1:]
            neighbors.add(new_word)
        
        # Insertions (only try inserting letters from target word)
        for i in range(length + 1):
            if i < len(word2):
                new_word = current[:i] + word2[i] + current[i:]
                neighbors.add(new_word)
        
        # Substitutions (only try substituting with target letters)
        for i in range(min(length, len(word2))):
            if current[i] != word2[i]:
                new_word = current[:i] + word2[i] + current[i+1:]
                neighbors.add(new_word)
        
        # Transpositions (only adjacent swaps that match target)
        for i in range(length - 1):
            if (i + 1 < len(word2) and 
                current[i] == word2[i+1] and 
                current[i+1] == word2[i]):
                new_word = current[:i] + current[i+1] + current[i] + current[i+2:]
                neighbors.add(new_word)
        
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor], remaining - 1))
    
    return f"{word1} {max_dist}+ (no path found)"

with open('answers.txt', 'w') as file:
    for w1, w2, dist in tqdm(read_data()):
        path =  find_correction_path(w1, w2, dist)
        file.write(path + '\n')
