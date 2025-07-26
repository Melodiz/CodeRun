pub fn solution(n: i32, a: &mut Vec<i32>) -> i32 {
    a.sort();

    let mut left = 0;
    let mut max_keep = 0;
    let n_usize = n as usize;

    for right in 0..n_usize {
        while a[right] - a[left] >= n {
            left += 1;
        }

        let current_keep = (right - left + 1) as i32;
        if current_keep > max_keep {
            max_keep = current_keep;
        }
    }

    let min_moves = n - max_keep;
    min_moves
}