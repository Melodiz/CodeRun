# Solution for https://coderun.yandex.ru/problem/hipuy
# Other solutions: https://github.com/Melodiz/CodeRun

class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def parent(self, i):
        return (i - 1) // 2
        
    def left_child(self, i):
        return 2 * i + 1
        
    def right_child(self, i):
        return 2 * i + 2
        
    def sift_up(self, i):
        parent_idx = self.parent(i)
        if i > 0 and self.heap[parent_idx] < self.heap[i]:
            self.heap[i], self.heap[parent_idx] = self.heap[parent_idx], self.heap[i]
            self.sift_up(parent_idx)
            
    def sift_down(self, i):
        max_index = i
        left = self.left_child(i)
        
        if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
            max_index = left
            
        right = self.right_child(i)
        if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
            max_index = right
            
        if i != max_index:
            self.heap[i], self.heap[max_index] = self.heap[max_index], self.heap[i]
            self.sift_down(max_index)
            
    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)
        
    def extract_max(self):
        if not self.heap:
            return None
            
        max_value = self.heap[0]
        
        # Replace the root with the last element
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        # If the heap is not empty, sift down the new root
        if self.heap:
            self.sift_down(0)
            
        return max_value

def main():
    n = int(input())
    heap = MaxHeap()
    
    for _ in range(n):
        command = input().split()
        
        if command[0] == '0':  # Insert
            value = int(command[1])
            heap.insert(value)
        elif command[0] == '1':  # Extract
            max_value = heap.extract_max()
            print(max_value)

if __name__ == "__main__":
    main()