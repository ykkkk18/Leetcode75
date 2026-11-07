"""Blind 75 · 专题 10：堆 Heap（第 72～73 集）"""
import heapq
from typing import List


# ---------- 347. 前 K 个高频元素（桶排序，O(n)） ----------
# 出现次数最多也就 n 次 -> 开 n+1 个桶，freq[次数] = 出现这么多次的数；从高频桶往低频桶收集
def top_k_frequent(nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for _ in range(len(nums) + 1)]
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
    return res


# 对比：堆的写法 O(n log k)
def top_k_frequent_heap(nums: List[int], k: int) -> List[int]:
    count = {}
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    return heapq.nlargest(k, count.keys(), key=count.get)


# ---------- 295. 数据流的中位数（Hard） ----------
# small：最大堆（存相反数），放较小的一半；large：最小堆，放较大的一半
# 保持：small 里每个数 <= large 里每个数；两边个数相差不超过 1
class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)                  # 默认先放进 small
        if self.small and self.large and -self.small[0] > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))   # 顺序不对就挪过去
        if len(self.small) > len(self.large) + 1:          # 个数不平衡就挪一个
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        if len(self.large) > len(self.small):
            return float(self.large[0])
        return (-self.small[0] + self.large[0]) / 2


if __name__ == "__main__":
    print("347 top_k_frequent([1,1,1,2,2,3], 2) ->", top_k_frequent([1, 1, 1, 2, 2, 3], 2),
          "| 堆版 ->", top_k_frequent_heap([1, 1, 1, 2, 2, 3], 2), "| ([1], 1) ->", top_k_frequent([1], 1))
    mf, out = MedianFinder(), []
    for x in (1, 2, 3, 6, 5):
        mf.addNum(x)
        out.append(mf.findMedian())
    print("295 依次加入 1,2,3,6,5，每次的中位数 ->", out)
