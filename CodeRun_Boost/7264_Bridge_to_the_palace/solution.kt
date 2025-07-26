fun solution(n: Int, a: IntArray): Int {
    a.sort()

    var left = 0
    var maxKeep = 0

    for (right in 0 until n) {
        while (a[right] - a[left] >= n) {
            left++
        }

        val currentKeep = right - left + 1
        if (currentKeep > maxKeep) {
            maxKeep = currentKeep
        }
    }

    val minMoves = n - maxKeep
    return minMoves
}