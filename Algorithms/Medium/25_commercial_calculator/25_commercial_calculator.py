class MinHeap:
    def __init__(self):
        self.heap = []

    def add(self, n):
        self.heap.append(n)
        self._sift_up(len(self.heap) - 1)

    def pop_least(self):
        if not self.heap:
            return -1
        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self._sift_down(0)
        return min_value

    def _sift_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._sift_up(parent)

    def _sift_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._sift_down(smallest)

    def is_empty(self):
        return len(self.heap) == 0


def main():
    n = int(input())
    heap = MinHeap()
    numbers = list(map(int, input().split()))
    for num in numbers:
        heap.add(num)
    total_cost = 0
    while len(heap.heap) > 1:
        a = heap.pop_least()
        b = heap.pop_least()
        total_cost += (a + b) * 0.05
        heap.add(a + b)
    print(f"{total_cost:.2f}")


if __name__ == "__main__":
    main()