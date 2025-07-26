import kotlin.math.min

private fun check(n: Long, m: Long, k: Long): Boolean {
    return (k * k <= n + m) && ((k * k) / 2 <= min(n, m))
}

fun solve(n: Int, m: Int): Int {
    var left: Long = 0
    var right: Long = 150000
    var ans: Long = 0

    val n_long = n.toLong()
    val m_long = m.toLong()

    while (left <= right) {
        val mid = left + (right - left) / 2

        if (check(n_long, m_long, mid)) {
            ans = mid
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    return ans.toInt()
}