"""Blind 75 · 专题 2：位运算 Binary（第 11～14、75 集）"""
from typing import List


# ---------- 191. 位 1 的个数 ----------
# 解法 1：逐位检查最低位 (n & 1 或 n % 2)，再右移一位   O(32)
def hamming_weight(n: int) -> int:
    res = 0
    while n:
        res += n & 1
        n >>= 1
    return res


# 解法 2：n & (n - 1) 每次消掉最右边的那个 1，循环次数 = 1 的个数
def hamming_weight_fast(n: int) -> int:
    res = 0
    while n:
        n &= n - 1
        res += 1
    return res


# ---------- 338. 比特位计数（DP） ----------
# 最高有效位 offset 是 2 的幂：dp[i] = 1 + dp[i - offset]
# 例：dp[5]=dp[101b] = 1 + dp[5-4] = 1 + dp[1]
def count_bits(n: int) -> List[int]:
    dp = [0] * (n + 1)
    offset = 1
    for i in range(1, n + 1):
        if offset * 2 == i:            # 到了下一个 2 的幂
            offset = i
        dp[i] = 1 + dp[i - offset]
    return dp


# 另一种常见写法：dp[i] = dp[i >> 1] + (i & 1)
def count_bits_shift(n: int) -> List[int]:
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp


# ---------- 268. 丢失的数字 ----------
# 解法 1：异或。相同的数异或为 0，把 0..n 和数组里的数全部异或，剩下的就是缺失的数
def missing_number(nums: List[int]) -> int:
    res = len(nums)
    for i, x in enumerate(nums):
        res ^= i ^ x
    return res


# 解法 2：求和差。sum(0..n) - sum(nums)，边加边减避免溢出（视频里的写法）
def missing_number_sum(nums: List[int]) -> int:
    res = len(nums)
    for i, x in enumerate(nums):
        res += i - x
    return res


# ---------- 190. 颠倒二进制位 ----------
# 依次取出第 i 位，放到第 31 - i 位上
def reverse_bits(n: int) -> int:
    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        res |= bit << (31 - i)
    return res


# ---------- 371. 两整数之和（不用 + 和 -） ----------
# 异或 = 不进位的加法；与运算再左移一位 = 进位。反复相加直到没有进位
# Python 的整数没有位数上限，要用 32 位掩码模拟（视频里用 Java 写，就是因为这个）
def get_sum(a: int, b: int) -> int:
    mask = 0xFFFFFFFF
    while b & mask:
        a, b = a ^ b, (a & b) << 1
    a &= mask
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)   # 还原成有符号数


if __name__ == "__main__":
    n = 0b00000000000000000000000000001011
    print("191 hamming_weight(0b1011) ->", hamming_weight(n), "| n&(n-1) 版 ->", hamming_weight_fast(n))
    print("191 hamming_weight(0b10000000) ->", hamming_weight(128))
    print("338 count_bits(5) ->", count_bits(5), "| 移位版 ->", count_bits_shift(5))
    print("338 count_bits(8) ->", count_bits(8))
    print("268 missing_number([3,0,1]) ->", missing_number([3, 0, 1]),
          "| [9,6,4,2,3,5,7,0,1] ->", missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]),
          "| 求和版 ->", missing_number_sum([3, 0, 1]))
    x = 0b00000010100101000001111010011100
    print("190 reverse_bits(43261596) ->", reverse_bits(x), f"(二进制 {reverse_bits(x):032b})")
    print("371 get_sum(1, 2) ->", get_sum(1, 2), "| get_sum(2, 3) ->", get_sum(2, 3),
          "| get_sum(-2, 3) ->", get_sum(-2, 3), "| get_sum(-5, -7) ->", get_sum(-5, -7))
