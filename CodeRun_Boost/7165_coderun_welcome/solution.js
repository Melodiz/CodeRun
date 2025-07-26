function check(n, m, k) {
    // All numbers in JS are 64-bit floats, which can safely handle the integer math here.
    return (k * k <= n + m) && (Math.floor((k * k) / 2) <= Math.min(n, m));
}

function solution(n, m) {
    let left = 0;
    let right = 150000;
    let ans = 0;

    while (left <= right) {
        let mid = Math.floor(left + (right - left) / 2);

        if (check(n, m, mid)) {
            ans = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return ans;
}

// Export the solution function for Node.js environments
module.exports = solution;