function solution(n, m, swaps) {
    let positions = Array.from({ length: 2 * n }, (_, i) => i + 1);

    let methodsOnLeftCount = n;
    let result = new Array(m);

    for (let i = 0; i < m; i++) {
        const p1Orig = swaps[2 * i];
        const p2Orig = swaps[2 * i + 1];

        const p1Idx = p1Orig - 1;
        const p2Idx = p2Orig - 1;

        const p1IsLeft = p1Idx < n;
        const p2IsLeft = p2Idx < n;

        if (p1IsLeft !== p2IsLeft) {
            const guard1 = positions[p1Idx];
            const guard2 = positions[p2Idx];

            const guard1IsMethod = guard1 <= n;
            const guard2IsMethod = guard2 <= n;

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

        [positions[p1Idx], positions[p2Idx]] = [positions[p2Idx], positions[p1Idx]];
        result[i] = methodsOnLeftCount;
    }

    return result;
}

module.exports = solution;