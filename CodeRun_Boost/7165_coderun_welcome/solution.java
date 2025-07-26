class Solution {
    // check function uses long to prevent overflow.
    public boolean check(long n, long m, long k) {
        return (k * k <= n + m) && ((k * k) / 2 <= Math.min(n, m));
    }

    // Method renamed to 'solve' and signature changed to use int as per the error log.
    public int solve(int n, int m) {
        long left = 0;
        long right = 150000;
        long ans = 0;

        // Use long for the binary search logic to avoid overflow.
        long n_long = n;
        long m_long = m;

        while (left <= right) {
            long mid = left + (right - left) / 2;

            if (check(n_long, m_long, mid)) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        // Cast the result back to int.
        return (int)ans;
    }
}