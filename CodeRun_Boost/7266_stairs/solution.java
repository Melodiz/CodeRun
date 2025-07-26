import java.util.Arrays;

class Solution {
    public int[] solve(int n, int[] a) {
        int[] result = new int[n + 1];
        if (n == 0) {
            return new int[0];
        }
        if (n == 1) {
            result[0] = 1;
            result[1] = a[0];
            return result;
        }

        int[] dpPlus = new int[n];
        int[] dpMinus = new int[n];
        dpPlus[0] = a[0];
        dpMinus[0] = -a[0];

        for (int i = 1; i < n; ++i) {
            int currentPlus = a[i];
            int currentMinus = -a[i];
            boolean plusOk = false;
            boolean minusOk = false;
            
            if (dpPlus[i-1] != Integer.MAX_VALUE && dpPlus[i-1] <= currentPlus) plusOk = true;
            if (dpMinus[i-1] != Integer.MAX_VALUE && dpMinus[i-1] <= currentPlus) plusOk = true;

            if (dpPlus[i-1] != Integer.MAX_VALUE && dpPlus[i-1] <= currentMinus) minusOk = true;
            if (dpMinus[i-1] != Integer.MAX_VALUE && dpMinus[i-1] <= currentMinus) minusOk = true;

            if (!plusOk && !minusOk) {
                return new int[n + 1];
            }
            
            dpPlus[i] = plusOk ? currentPlus : Integer.MAX_VALUE;
            dpMinus[i] = minusOk ? currentMinus : Integer.MAX_VALUE;
        }

        result[0] = 1;
        int current;

        if (dpPlus[n - 1] != Integer.MAX_VALUE && dpMinus[n-1] != Integer.MAX_VALUE) {
            current = Math.min(dpPlus[n-1], dpMinus[n-1]);
        } else if (dpPlus[n-1] != Integer.MAX_VALUE) {
            current = dpPlus[n-1];
        } else {
            current = dpMinus[n-1];
        }
        result[n] = current;


        for (int i = n - 2; i >= 0; --i) {
            int prevPlus = dpPlus[i];
            int prevMinus = dpMinus[i];

            if (prevPlus != Integer.MAX_VALUE && prevPlus <= current) {
                if (prevMinus != Integer.MAX_VALUE && prevMinus <= current) {
                    current = Math.min(prevPlus, prevMinus);
                } else {
                    current = prevPlus;
                }
            } else if (prevMinus != Integer.MAX_VALUE && prevMinus <= current) {
                current = prevMinus;
            }
            result[i+1] = current;
        }

        return result;
    }
}