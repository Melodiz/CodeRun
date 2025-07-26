pub fn solution(n: i32, m: i32, swaps: &Vec<i32>) -> Vec<i32> {
    let n_usize = n as usize;
    let m_usize = m as usize;
    let mut positions: Vec<i32> = (1..=(2 * n)).collect();

    let mut methods_on_left_count = n;
    let mut result = vec![0; m_usize];

    for i in 0..m_usize {
        let p1_orig = swaps[2 * i];
        let p2_orig = swaps[2 * i + 1];

        let p1_idx = (p1_orig - 1) as usize;
        let p2_idx = (p2_orig - 1) as usize;

        let p1_is_left = p1_idx < n_usize;
        let p2_is_left = p2_idx < n_usize;

        if p1_is_left != p2_is_left {
            let guard1 = positions[p1_idx];
            let guard2 = positions[p2_idx];

            let guard1_is_method = guard1 <= n;
            let guard2_is_method = guard2 <= n;

            if p1_is_left {
                if guard1_is_method {
                    methods_on_left_count -= 1;
                }
                if guard2_is_method {
                    methods_on_left_count += 1;
                }
            } else {
                if guard2_is_method {
                    methods_on_left_count -= 1;
                }
                if guard1_is_method {
                    methods_on_left_count += 1;
                }
            }
        }

        positions.swap(p1_idx, p2_idx);
        result[i] = methods_on_left_count;
    }

    result
}