import Foundation

public func solve(n: Int, m: Int, swaps: [Int]) -> [Int] {
    var positions = Array(1...(2 * n))
    
    var methodsOnLeftCount = n
    var result = [Int](repeating: 0, count: m)
    
    for i in 0..<m {
        let p1Orig = swaps[2 * i]
        let p2Orig = swaps[2 * i + 1]
        
        let p1Idx = p1Orig - 1
        let p2Idx = p2Orig - 1
        
        let p1IsLeft = p1Idx < n
        let p2IsLeft = p2Idx < n
        
        if p1IsLeft != p2IsLeft {
            let guard1 = positions[p1Idx]
            let guard2 = positions[p2Idx]
            
            let guard1IsMethod = guard1 <= n
            let guard2IsMethod = guard2 <= n
            
            if p1IsLeft {
                if guard1IsMethod {
                    methodsOnLeftCount -= 1
                }
                if guard2IsMethod {
                    methodsOnLeftCount += 1
                }
            } else {
                if guard2IsMethod {
                    methodsOnLeftCount -= 1
                }
                if guard1IsMethod {
                    methodsOnLeftCount += 1
                }
            }
        }
        
        positions.swapAt(p1Idx, p2Idx)
        result[i] = methodsOnLeftCount
    }
    
    return result
}