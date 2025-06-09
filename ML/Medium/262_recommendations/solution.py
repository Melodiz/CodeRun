# Solution for https://coderun.yandex.ru/problem/recommendations
# Other solutions: https://github.com/Melodiz/CodeRun
import heapq

def main():
    n, m = map(int,input().split())

    b = [int(input()) for _ in range(n)]

    items_by_type = [[] for _ in range(m)]
    for i in range(n):
        items_by_type[b[i]].append(i)

    type_pointers = [0] * m
    
    pq = []
    
    for type_id in range(m):
        if type_pointers[type_id] < len(items_by_type[type_id]):
            original_index = items_by_type[type_id][type_pointers[type_id]]
            heapq.heappush(pq, (original_index, type_id))

    result = []
    last_chosen_type = -1

    while pq:
        temp_skipped_items = []
        
        found_valid_item_in_this_step = False

        while pq:
            current_original_index, current_type = heapq.heappop(pq)

            if current_type != last_chosen_type:
                result.append(current_original_index)
                last_chosen_type = current_type
                found_valid_item_in_this_step = True

                type_pointers[current_type] += 1
                if type_pointers[current_type] < len(items_by_type[current_type]):
                    next_original_index = items_by_type[current_type][type_pointers[current_type]]
                    heapq.heappush(pq, (next_original_index, current_type))
                
                break
            else:
                temp_skipped_items.append((current_original_index, current_type))
        
        for item in temp_skipped_items:
            heapq.heappush(pq, item)
            
        if not found_valid_item_in_this_step:
            break
    print(*(result))

if __name__ == "__main__":
    main()