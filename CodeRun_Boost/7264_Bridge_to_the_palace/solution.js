function solution(n, a) {
    a.sort((x, y) => x - y);

    let left = 0;
    let maxKeep = 0;

    for (let right = 0; right < n; ++right) {
        while (a[right] - a[left] >= n) {
            left++;
        }

        let currentKeep = right - left + 1;
        if (currentKeep > maxKeep) {
            maxKeep = currentKeep;
        }
    }

    let minMoves = n - maxKeep;
    return minMoves;
}

module.exports = solution;