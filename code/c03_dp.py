"""Blind 75 · 专题 3：动态规划 Dynamic Programming（第 15～25 集）"""
from typing import List


# ---------- 70. 爬楼梯 ----------
# 从终点倒推：dp[i] = dp[i+1] + dp[i+2]，本质就是斐波那契。只需两个变量
def climb_stairs(n: int) -> int:
    one, two = 1, 1                      # 视频里从底部往回算：最后两级都只有 1 种
    for _ in range(n - 1):
        one, two = one + two, one
    return one


# ---------- 322. 零钱兑换（Bottom-up） ----------
# dp[a] = 凑出金额 a 需要的最少硬币数 = 1 + min(dp[a - c])
# 贪心（先用最大面值）不一定对：coins=[1,3,4,5], amount=7 -> 贪心 5+1+1=3 枚，最优 3+4=2 枚
def coin_change(coins: List[int], amount: int) -> int:
    dp = [amount + 1] * (amount + 1)     # amount+1 相当于"无穷大"
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[amount] if dp[amount] != amount + 1 else -1


# ---------- 300. 最长递增子序列 ----------
# 从后往前：LIS[i] = 以 i 开头的最长递增子序列长度 = 1 + max(LIS[j])，j > i 且 nums[j] > nums[i]
def length_of_lis(nums: List[int]) -> int:
    lis = [1] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                lis[i] = max(lis[i], 1 + lis[j])
    return max(lis)


# 进阶 O(n log n)：维护"长度为 k 的递增子序列的最小结尾"，二分替换（视频没讲，面试加分）
def length_of_lis_fast(nums: List[int]) -> int:
    import bisect
    tails = []
    for x in nums:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


# ---------- 1143. 最长公共子序列 ----------
# 二维表，从右下往左上填：字符相等 -> 1 + 右下；不等 -> max(右, 下)
def longest_common_subsequence(text1: str, text2: str) -> int:
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[0][0]


# ---------- 139. 单词拆分 ----------
# dp[i] = s[i:] 能否被拆分。从后往前：某个单词 w 恰好匹配 s[i:i+len(w)] 且 dp[i+len(w)] 为真
def word_break(s: str, word_dict: List[str]) -> bool:
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True                    # 空串：base case
    for i in range(len(s) - 1, -1, -1):
        for w in word_dict:
            if s[i:i + len(w)] == w and dp[i + len(w)]:
                dp[i] = True
                break
    return dp[0]


# ---------- 39. 组合总和（回溯） ----------
# 决策树：每一步要么"还用第 i 个数"，要么"以后再也不用第 i 个数"（i+1），这样不会产生重复组合
def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    res = []

    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target:
            return
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])       # 继续用 candidates[i]
        cur.pop()
        dfs(i + 1, cur, total)                    # 不再用 candidates[i]

    dfs(0, [], 0)
    return res


# ---------- 198. 打家劫舍 ----------
# rob = max(当前房子 + 隔一间之前的最优, 上一间的最优)，只需两个变量
def rob(nums: List[int]) -> int:
    rob1, rob2 = 0, 0                    # [rob1, rob2, n, n+1, ...]
    for n in nums:
        rob1, rob2 = rob2, max(n + rob1, rob2)
    return rob2


# ---------- 213. 打家劫舍 II（房子围成一圈） ----------
# 首尾不能同时偷 -> 去掉第一间算一次，去掉最后一间算一次，取较大值（只有一间房要单独处理）
def rob_circle(nums: List[int]) -> int:
    return max(nums[0], rob(nums[1:]), rob(nums[:-1]))


# ---------- 91. 解码方法 ----------
# dp[i] = s[i:] 的解码数。单个字符（非 '0'）-> + dp[i+1]；两个字符在 10~26 -> + dp[i+2]
def num_decodings(s: str) -> int:
    dp = {len(s): 1}
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "0":
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]
        if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
            dp[i] += dp[i + 2]
    return dp[0]


# ---------- 62. 不同路径 ----------
# 每个格子的路径数 = 右边 + 下边。只需保留一行
def unique_paths(m: int, n: int) -> int:
    row = [1] * n                        # 最底下一行全是 1
    for _ in range(m - 1):
        new_row = [1] * n
        for j in range(n - 2, -1, -1):
            new_row[j] = new_row[j + 1] + row[j]
        row = new_row
    return row[0]


# ---------- 55. 跳跃游戏（贪心） ----------
# 把"终点"从最后往前挪：如果从 i 能跳到当前终点，那 i 就成了新的终点
def can_jump(nums: List[int]) -> bool:
    goal = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0


if __name__ == "__main__":
    print("70   climb_stairs(2), (3), (5) ->", climb_stairs(2), climb_stairs(3), climb_stairs(5))
    print("322  coin_change([1,2,5], 11) ->", coin_change([1, 2, 5], 11), "| ([2], 3) ->", coin_change([2], 3),
          "| ([1,3,4,5], 7) ->", coin_change([1, 3, 4, 5], 7))
    a = [10, 9, 2, 5, 3, 7, 101, 18]
    print("300  length_of_lis([10,9,2,5,3,7,101,18]) ->", length_of_lis(a), "| O(n log n) 版 ->", length_of_lis_fast(a))
    print("1143 longest_common_subsequence('abcde', 'ace') ->", longest_common_subsequence("abcde", "ace"))
    print("139  word_break('neetcode', ['neet','code']) ->", word_break("neetcode", ["neet", "code"]),
          "| ('catsandog', [cats,dog,sand,and,cat]) ->", word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print("39   combination_sum([2,3,6,7], 7) ->", combination_sum([2, 3, 6, 7], 7))
    print("198  rob([1,2,3,1]) ->", rob([1, 2, 3, 1]), "| rob([2,7,9,3,1]) ->", rob([2, 7, 9, 3, 1]))
    print("213  rob_circle([2,3,2]) ->", rob_circle([2, 3, 2]), "| [1,2,3,1] ->", rob_circle([1, 2, 3, 1]), "| [1] ->", rob_circle([1]))
    print("91   num_decodings('12'), ('226'), ('06') ->", num_decodings("12"), num_decodings("226"), num_decodings("06"))
    print("62   unique_paths(3, 7) ->", unique_paths(3, 7), "| (3, 2) ->", unique_paths(3, 2))
    print("55   can_jump([2,3,1,1,4]) ->", can_jump([2, 3, 1, 1, 4]), "| [3,2,1,0,4] ->", can_jump([3, 2, 1, 0, 4]))
