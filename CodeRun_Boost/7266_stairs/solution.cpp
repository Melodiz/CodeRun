#include <vector>
#include <climits>

using namespace std;

vector<int> solution(int n, const vector<int>& a) {
    vector<int> result(n + 1, 0);
    if (n == 1) {
        result[0] = 1;
        result[1] = a[0];
        return result;
    }

    vector<int> dp_plus(n, 0);
    vector<int> dp_minus(n, 0);
    dp_plus[0] = a[0];
    dp_minus[0] = -a[0];

    for (int i = 1; i < n; ++i) {
        int current_plus = a[i];
        int current_minus = -a[i];
        bool plus_ok = false;
        bool minus_ok = false;

        if (dp_plus[i-1] <= current_plus) plus_ok = true;
        if (dp_minus[i-1] <= current_plus) plus_ok = true;

        if (dp_plus[i-1] <= current_minus) minus_ok = true;
        if (dp_minus[i-1] <= current_minus) minus_ok = true;

        if (!plus_ok && !minus_ok) return result;

        if (plus_ok && minus_ok) {
            dp_plus[i] = current_plus;
            dp_minus[i] = current_minus;
        } else if (plus_ok) {
            dp_plus[i] = current_plus;
            dp_minus[i] = INT_MAX;
        } else {
            dp_plus[i] = INT_MAX;
            dp_minus[i] = current_minus;
        }
    }

    result[0] = 1;
    int current = INT_MAX;
    for (int i = n - 1; i >= 0; --i) {
        if (i == n - 1) {
            if (dp_plus[i] != INT_MAX) {
                result[i+1] = dp_plus[i];
                current = dp_plus[i];
            } else {
                result[i+1] = dp_minus[i];
                current = dp_minus[i];
            }
        } else {
            if (dp_plus[i] <= current) {
                result[i+1] = dp_plus[i];
                current = dp_plus[i];
            } else {
                result[i+1] = dp_minus[i];
                current = dp_minus[i];
            }
        }
    }

    return result;
}