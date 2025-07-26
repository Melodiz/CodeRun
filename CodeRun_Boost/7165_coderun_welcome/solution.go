package main

import "math"

// check function uses int64 to prevent overflow during calculations.
func check(n int64, m int64, k int64) bool {
	return (k*k <= n+m) && ((k*k)/2 <= int64(math.Min(float64(n), float64(m))))
}

// solution function accepts standard integers as per the error log.
func solution(n int, m int) int {
	var left int64 = 0
	var right int64 = 150000
	var ans int64 = 0

	// Convert inputs to int64 for the binary search and check.
	var n_i64 int64 = int64(n)
	var m_i64 int64 = int64(m)

	for left <= right {
		mid := left + (right-left)/2

		if check(n_i64, m_i64, mid) {
			ans = mid
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	// Cast the final answer back to int.
	return int(ans)
}