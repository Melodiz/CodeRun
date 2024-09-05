def read_input():
    start = input().strip()
    end = input().strip()
    typos = []
    for _ in range(int(input())):
        typos.append(tuple(input().strip().split()))
    return start, end, typos


def brute(start, end, typos):
    if start == end:
        return 0 
    l1 = apply_typos_end([end], typos)
    if start in l1:
        return 1
    l2 = apply_typos_end(l1, typos)
    if start in l2:
        return 2
    l3 = apply_typos_end(l2, typos)
    if start in l3:
        return 3
    l4 = apply_typos_end(l3, typos)
    if start in l4:
        return 4
    return -1

def apply_typo_start(word, typo):
    result = set()
    result.add(word)
    start_index = word.find(typo[0])
    while start_index != -1:
        result.add(word[:start_index]+typo[1]+word[start_index+len(typo[0]):])
        start_index = word.find(typo[0], start_index+1)
    if not result:
        return word
    return result

def apply_typo_end(word, typo):
    result = set()
    result.add(word)
    start_index = word.find(typo[1])
    while start_index != -1:
        result.add(word[:start_index]+typo[0]+word[start_index+len(typo[1]):])
        start_index = word.find(typo[1], start_index+1)
    if not result:
        return word
    return result

def apply_typos_start(word_set, typos):
    # generate all possible words with 1 typo (from typos)
    result = set()
    for word in word_set:
        for typo in typos:
            result.update(apply_typo_start(word, typo))
    return result

def apply_typos_end(word_set, typos):
    # generate all possible words with 1 typo (from typos)
    result = set()
    for word in word_set:
        for typo in typos:
            result.update(apply_typo_end(word, typo))
    return result

def process(start, end, typos):
    if start == end:
        return 0
    l1_start = apply_typos_start([start], typos)
    if end in l1_start:
        return 1
    t1_end = apply_typos_end([end], typos)
    if l1_start.intersection(t1_end):
        return 2
    t2_start = apply_typos_start(l1_start, typos)
    if t1_end.intersection(t2_start):
        return 3
    t2_end = apply_typos_end(t1_end, typos)
    if t2_start.intersection(t2_end):
        return 4
    print(f'len t1_start: {len(l1_start)}, len t1_end: {len(t1_end)}, len t2_start: {len(t2_start)}, len t2_end: {len(t2_end)}')
    return -1


def main():
    start, end, typos = read_input()
    # print(process(start, end, typos))
    print(brute(start, end, typos))

### Hahaha. I've just tested this block to make sure there are no mistakes in apply_typos and apply_typos_end functions.
### But eventually, the brute force solution was accepted. Moreover, the brute force solution 
### took at most 700ms of 5000 ms given. How funny!

if __name__ == "__main__":
    main()
