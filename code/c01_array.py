"""Blind 75 · 专题 1：数组 Array（第 1～10 集）"""
from typing import List


# ---------- 1. 两数之和 Two Sum ----------
# 哈希表：值 -> 下标。对每个数，先查 target - n 是否出现过，再把自己存进去
def two_sum(nums: List[int], target: int) -> List[int]:
    prev = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev:
            return [prev[diff], i]
        prev[n] = i
    return []


# ---------- 121. 买卖股票的最佳时机 ----------
# 双指针 / 滑动窗口：l 是买入日（始终指向目前最低价），r 是卖出日
def max_profit(prices: List[int]) -> int:
    l, best = 0, 0
    for r in range(1, len(prices)):
        if prices[r] > prices[l]:
            best = max(best, prices[r] - prices[l])
        else:
            l = r                      # 发现更低的价格：直接把买入日挪到这里
    return best


# ---------- 217. 存在重复元素 ----------
# 三种解法：暴力 O(n^2) / 排序后比较相邻 O(n log n) / 哈希集合 O(n)
def contains_duplicate(nums: List[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


def contains_duplicate_sort(nums: List[int]) -> bool:
    s = sorted(nums)
    return any(s[i] == s[i - 1] for i in range(1, len(s)))


# ---------- 238. 除自身以外数组的乘积 ----------
# 不能用除法：answer[i] = 前缀积(i 左边) * 后缀积(i 右边)
# 先从左到右把前缀积写进 res，再从右到左乘上后缀积 -> 额外空间 O(1)
def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1] * n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res


# ---------- 53. 最大子数组和（Kadane） ----------
# 当前和一旦变成负数，它只会拖累后面 -> 丢掉（重置为 0）
def max_sub_array(nums: List[int]) -> int:
    best, cur = nums[0], 0
    for n in nums:
        if cur < 0:
            cur = 0
        cur += n
        best = max(best, cur)
    return best


# ---------- 152. 乘积最大子数组 ----------
# 负数会让最小值翻身成最大值 -> 同时维护"以当前结尾的最大积和最小积"
def max_product(nums: List[int]) -> int:
    res = max(nums)
    cur_max = cur_min = 1
    for n in nums:
        candidates = (n * cur_max, n * cur_min, n)
        cur_max, cur_min = max(candidates), min(candidates)   # 必须同时更新
        res = max(res, cur_max)
    return res


# ---------- 153. 寻找旋转排序数组中的最小值 ----------
# 二分：数组分成"左段（较大）"和"右段（较小）"，最小值在右段开头
def find_min(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    res = nums[0]
    while l <= r:
        if nums[l] < nums[r]:          # 这一段已经整体有序，最左边就是最小
            res = min(res, nums[l])
            break
        m = (l + r) // 2
        res = min(res, nums[m])
        if nums[m] >= nums[l]:         # m 在左段 -> 最小值在右边
            l = m + 1
        else:                          # m 在右段 -> 往左找
            r = m - 1
    return res


# ---------- 33. 搜索旋转排序数组 ----------
# 先判断 m 落在左段还是右段，再判断 target 在不在"有序的那一半"里
def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[l] <= nums[m]:                         # 左半边有序
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:                                          # 右半边有序
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1


# ---------- 15. 三数之和 ----------
# 排序 -> 固定第一个数 a -> 剩下变成"有序数组的两数之和"（167 题），用相向双指针
# 去重：a 和上一个相同就跳过；找到一组后，左指针跳过相同的值
def three_sum(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    res = []
    for i, a in enumerate(nums):
        if a > 0:                       # 已排序，后面都是正数，不可能和为 0
            break
        if i > 0 and a == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = a + nums[l] + nums[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
    return res


# ---------- 11. 盛最多水的容器 ----------
# 面积由短板决定：移动较短的一边，才可能变大
def max_area(height: List[int]) -> int:
    l, r, best = 0, len(height) - 1, 0
    while l < r:
        best = max(best, (r - l) * min(height[l], height[r]))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return best


if __name__ == "__main__":
    print("1    two_sum([2,7,11,15], 9) ->", two_sum([2, 7, 11, 15], 9))
    print("121  max_profit([7,1,5,3,6,4]) ->", max_profit([7, 1, 5, 3, 6, 4]), "| [7,6,4,3,1] ->", max_profit([7, 6, 4, 3, 1]))
    print("217  contains_duplicate([1,2,3,1]) ->", contains_duplicate([1, 2, 3, 1]),
          "| [1,2,3,4] ->", contains_duplicate([1, 2, 3, 4]), "| 排序版 ->", contains_duplicate_sort([1, 2, 3, 1]))
    print("238  product_except_self([1,2,3,4]) ->", product_except_self([1, 2, 3, 4]))
    print("53   max_sub_array([-2,1,-3,4,-1,2,1,-5,4]) ->", max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print("152  max_product([2,3,-2,4]) ->", max_product([2, 3, -2, 4]), "| [-2,3,-4] ->", max_product([-2, 3, -4]))
    print("153  find_min([3,4,5,1,2]) ->", find_min([3, 4, 5, 1, 2]), "| [4,5,6,7,0,1,2] ->", find_min([4, 5, 6, 7, 0, 1, 2]))
    print("33   search([4,5,6,7,0,1,2], 0) ->", search([4, 5, 6, 7, 0, 1, 2], 0), "| target=3 ->", search([4, 5, 6, 7, 0, 1, 2], 3))
    print("15   three_sum([-1,0,1,2,-1,-4]) ->", three_sum([-1, 0, 1, 2, -1, -4]))
    print("11   max_area([1,8,6,2,5,4,8,3,7]) ->", max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
