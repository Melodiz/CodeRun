use std::cmp;

// check function can remain private as it's only used within this module.
fn check(n: i64, m: i64, k: i64) -> bool {
    (k * k <= n + m) && ((k * k) / 2 <= cmp::min(n, m))
}

// solution function is made public with `pub` so it can be called from main.rs.
pub fn solution(n: i32, m: i32) -> i32 {
    let mut left: i64 = 0;
    let mut right: i64 = 150000;
    let mut ans: i64 = 0;

    let n_i64 = n as i64;
    let m_i64 = m as i64;

    while left <= right {
        let mid = left + (right - left) / 2;

        if check(n_i64, m_i64, mid) {
            ans = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    ans as i32
}