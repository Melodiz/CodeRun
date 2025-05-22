
/** @returns Boolean */  
module.exports = function(nums, k) {  
    const req = new Set();
    for (const num of nums) {
        if (req.has(num)) return true;
        req.add(k - num);
    }
    return false;
}