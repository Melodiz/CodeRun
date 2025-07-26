import Foundation

// check function uses Int64 to prevent overflow.
private func check(_ n: Int64, _ m: Int64, _ k: Int64) -> Bool {
    return (k * k <= n + m) && ((k * k) / 2 <= min(n, m))
}

// Updated function signature to require argument labels 'n' and 'm' during calls.
func solve(n: Int, m: Int) -> Int {
    var left: Int64 = 0
    var right: Int64 = 150000
    var ans: Int64 = 0

    // Convert inputs to Int64 for calculations.
    let n_i64 = Int64(n)
    let m_i64 = Int64(m)

    while left <= right {
        let mid = left + (right - left) / 2

        if check(n_i64, m_i64, mid) {
            ans = mid
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    // Convert result back to Int.
    return Int(ans)
}