package main

import "sort"

func solution(n int, a []int) int {
	sort.Ints(a)

	left := 0
	maxKeep := 0

	for right := 0; right < n; right++ {
		for a[right]-a[left] >= n {
			left++
		}

		currentKeep := right - left + 1
		if currentKeep > maxKeep {
			maxKeep = currentKeep
		}
	}

	minMoves := n - maxKeep
	return minMoves
}