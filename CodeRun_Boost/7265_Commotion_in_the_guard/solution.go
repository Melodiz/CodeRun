package main

func solve(n int, m int, swaps []int) []int {
	positions := make([]int, 2*n)
	for i := range positions {
		positions[i] = i + 1
	}

	methodsOnLeftCount := n
	result := make([]int, m)

	for i := 0; i < m; i++ {
		p1Orig := swaps[2*i]
		p2Orig := swaps[2*i+1]

		p1Idx := p1Orig - 1
		p2Idx := p2Orig - 1

		p1IsLeft := p1Idx < n
		p2IsLeft := p2Idx < n

		if p1IsLeft != p2IsLeft {
			guard1 := positions[p1Idx]
			guard2 := positions[p2Idx]

			guard1IsMethod := guard1 <= n
			guard2IsMethod := guard2 <= n

			if p1IsLeft {
				if guard1IsMethod {
					methodsOnLeftCount--
				}
				if guard2IsMethod {
					methodsOnLeftCount++
				}
			} else {
				if guard2IsMethod {
					methodsOnLeftCount--
				}
				if guard1IsMethod {
					methodsOnLeftCount++
				}
			}
		}

		positions[p1Idx], positions[p2Idx] = positions[p2Idx], positions[p1Idx]
		result[i] = methodsOnLeftCount
	}

	return result
}