fun solution(n: Int, m: Int, swaps: IntArray): IntArray {
    val positions = IntArray(2 * n) { it + 1 }

    var methodsOnLeftCount = n
    val result = IntArray(m)

    for (i in 0 until m) {
        val p1Orig = swaps[2 * i]
        val p2Orig = swaps[2 * i + 1]

        val p1Idx = p1Orig - 1
        val p2Idx = p2Orig - 1

        val p1IsLeft = p1Idx < n
        val p2IsLeft = p2Idx < n

        if (p1IsLeft != p2IsLeft) {
            val guard1 = positions[p1Idx]
            val guard2 = positions[p2Idx]

            val guard1IsMethod = guard1 <= n
            val guard2IsMethod = guard2 <= n

            if (p1IsLeft) {
                if (guard1IsMethod) {
                    methodsOnLeftCount--
                }
                if (guard2IsMethod) {
                    methodsOnLeftCount++
                }
            } else {
                if (guard2IsMethod) {
                    methodsOnLeftCount--
                }
                if (guard1IsMethod) {
                    methodsOnLeftCount++
                }
            }
        }

        val temp = positions[p1Idx]
        positions[p1Idx] = positions[p2Idx]
        positions[p2Idx] = temp

        result[i] = methodsOnLeftCount
    }

    return result
}