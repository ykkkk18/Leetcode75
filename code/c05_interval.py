"""Blind 75 · 专题 5：区间 Interval（第 34～38 集）"""
import heapq
from typing import List


# ---------- 57. 插入区间 ----------
# 三种情况：新区间完全在当前区间左边 / 完全在右边 / 重叠（合并，继续往后看）
def insert(intervals: List[List[int]], new: List[int]) -> List[List[int]]:
    res = []
    for i, cur in enumerate(intervals):
        if new[1] < cur[0]:                  # 新区间在左边，后面也不会再重叠
            res.append(new)
            return res + intervals[i:]
        elif new[0] > cur[1]:                # 新区间在右边，当前区间原样保留
            res.append(cur)
        else:                                # 重叠：合并成更大的新区间
            new = [min(new[0], cur[0]), max(new[1], cur[1])]
    res.append(new)
    return res


# ---------- 56. 合并区间 ----------
# 按起点排序；当前起点 <= 上一个终点 -> 重叠，更新终点为两者的较大值
def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals = sorted(intervals, key=lambda x: x[0])
    out = [intervals[0][:]]
    for start, end in intervals[1:]:
        last_end = out[-1][1]
        if start <= last_end:
            out[-1][1] = max(last_end, end)   # 注意取 max：[1,5] 和 [2,4] 合并后还是 [1,5]
        else:
            out.append([start, end])
    return out


# ---------- 435. 无重叠区间 ----------
# 按起点排序；遇到重叠时删掉"终点更大"的那个（贪心：留下的越早结束，后面越不容易重叠）
def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    intervals = sorted(intervals)
    res = 0
    prev_end = intervals[0][1]
    for start, end in intervals[1:]:
        if start >= prev_end:                # 不重叠（端点相接不算重叠）
            prev_end = end
        else:
            res += 1
            prev_end = min(end, prev_end)    # 保留终点更小的那个
    return res


# ---------- 252. 会议室（LeetCode 会员题） ----------
# 一个人能否参加所有会议 = 按开始时间排序后，相邻两个会议不重叠
def can_attend_meetings(intervals: List[List[int]]) -> bool:
    intervals = sorted(intervals)
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True


# ---------- 253. 会议室 II（LeetCode 会员题） ----------
# 解法 1（视频）：开始时间、结束时间分别排序，双指针扫时间轴，统计同时进行的会议数的最大值
def min_meeting_rooms(intervals: List[List[int]]) -> int:
    start = sorted(i[0] for i in intervals)
    end = sorted(i[1] for i in intervals)
    res = count = 0
    s = e = 0
    while s < len(intervals):
        if start[s] < end[e]:                # 先有会议开始
            s += 1
            count += 1
        else:                                # 先有会议结束（同一时刻先结束再开始）
            e += 1
            count -= 1
        res = max(res, count)
    return res


# 解法 2：最小堆存"正在进行的会议的结束时间"，堆的大小就是需要的房间数
def min_meeting_rooms_heap(intervals: List[List[int]]) -> int:
    heap = []
    for s, e in sorted(intervals):
        if heap and heap[0] <= s:            # 最早结束的会议已经结束，复用那间房
            heapq.heappop(heap)
        heapq.heappush(heap, e)
    return len(heap)


if __name__ == "__main__":
    print("57  insert([[1,3],[6,9]], [2,5]) ->", insert([[1, 3], [6, 9]], [2, 5]))
    print("57  insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) ->",
          insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    print("56  merge([[1,3],[2,6],[8,10],[15,18]]) ->", merge([[1, 3], [2, 6], [8, 10], [15, 18]]),
          "| [[1,5],[2,4]] ->", merge([[1, 5], [2, 4]]))
    print("435 erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]) ->", erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]),
          "| [[1,2],[1,2],[1,2]] ->", erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]))
    print("252 can_attend_meetings([[0,30],[5,10],[15,20]]) ->", can_attend_meetings([[0, 30], [5, 10], [15, 20]]),
          "| [[7,10],[2,4]] ->", can_attend_meetings([[7, 10], [2, 4]]))
    m = [[0, 30], [5, 10], [15, 20]]
    print("253 min_meeting_rooms([[0,30],[5,10],[15,20]]) ->", min_meeting_rooms(m), "| 堆版 ->", min_meeting_rooms_heap(m))
    m2 = [[0, 40], [5, 10], [15, 20], [5, 25]]
    print("253 min_meeting_rooms([[0,40],[5,10],[15,20],[5,25]]) ->", min_meeting_rooms(m2), "| 堆版 ->", min_meeting_rooms_heap(m2))
