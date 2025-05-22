# Solution for https://coderun.yandex.ru/problem/search-for-numbers/

def solution(k, nums):
    n = len(nums)
    req = set()
    for num in nums:
        if num in req: return True
        req.add(k - num)
    return False

if __name__ == "__main__":
    solution()
