#include <vector>
#include <numeric> // Required for std::iota

std::vector<int> solution(int n, int m, std::vector<int>& swaps) {
    std::vector<int> positions(2 * n);
    std::iota(positions.begin(), positions.end(), 1);

    int methodsOnLeftCount = n;

    std::vector<int> result(m);

    for (int i = 0; i < m; ++i) {
        int p1Orig = swaps[2 * i];
        int p2Orig = swaps[2 * i + 1];

        int p1Idx = p1Orig - 1;
        int p2Idx = p2Orig - 1;

        bool p1IsLeft = (p1Idx < n);
        bool p2IsLeft = (p2Idx < n);

        if (p1IsLeft != p2IsLeft) {
            int guard1 = positions[p1Idx];
            int guard2 = positions[p2Idx];

            bool guard1IsMethod = (guard1 <= n);
            bool guard2IsMethod = (guard2 <= n);

            if (p1IsLeft) {
                if (guard1IsMethod) {
                    methodsOnLeftCount--;
                }
                if (guard2IsMethod) {
                    methodsOnLeftCount++;
                }
            } else {
                if (guard2IsMethod) {
                    methodsOnLeftCount--;
                }
                if (guard1IsMethod) {
                    methodsOnLeftCount++;
                }
            }
        }

        std::swap(positions[p1Idx], positions[p2Idx]);

        result[i] = methodsOnLeftCount;
    }

    return result;
}