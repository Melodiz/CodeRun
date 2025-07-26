import Foundation

public func solve(n: Int, a: inout [Int]) -> Int {
    a.sort()

    var left = 0
    var maxKeep = 0

    for right in 0..<n {
        while a[right] - a[left] >= n {
            left += 1
        }

        let currentKeep = right - left + 1
        if currentKeep > maxKeep {
            maxKeep = currentKeep
        }
    }

    let minMoves = n - maxKeep
    return minMoves
}