# Blind 75 · NeetCode 视频讲解 · Python 学习笔记（合订本）

> 包含 7 天学习路径、10 个专题共 75 道题的笔记（含全部代码和运行结果）、全系列总结。


---

# 7 天学习路径

> 视频总时长约 16.5 小时，平均每天 2.4 小时。NeetCode 语速适中，**建议用 1.5 倍速观看**，这样每天约 1～2 小时视频，再加上 1.5～2 小时动手练习。
> 安排顺序：**先易后难**，前三天是线性结构，第 4、5 天是树，最后两天是图和 DP。这和播放列表的顺序不同，是为了循序渐进。

## 每天的固定流程

1. **先做题，再看视频**：每道题先自己想 10～15 分钟，至少写出暴力解，然后再看视频。带着问题看，收获最大。
2. **看视频**时打开对应的笔记，重点看"暴力解 → 关键观察 → 最优解"是怎么推出来的。
3. **运行代码**：`python code/cXX_xxx.py`，对照笔记里的运行结果。
4. **独立重写**：合上笔记，在 LeetCode 上把当天的题重新提交一遍，力求一次通过。
5. **自测**：回答当天的自测问题。

## 总览

| 天 | 专题 | 集数 | 题数 | 视频时长（1.5 倍速） |
| --- | --- | --- | --- | --- |
| Day 1 | 数组 + 位运算 | 1～14、75 | 15 | 170 分钟（约 113 分钟） |
| Day 2 | 字符串 | 49～57、74 | 10 | 134 分钟（约 89 分钟） |
| Day 3 | 链表 + 区间 + 矩阵 | 39～48、34～38 | 15 | 175 分钟（约 117 分钟） |
| Day 4 | 树（上）+ 堆 | 58～64、72～73 | 9 | 118 分钟（约 79 分钟） |
| Day 5 | 树（下）：BST 与 Trie + 图（上） | 65～71、26～29 | 11 | 160 分钟（约 107 分钟） |
| Day 6 | 图（下）+ DP（上） | 30～33、15～19 | 9 | 151 分钟（约 101 分钟） |
| Day 7 | DP（下）+ 总复习 | 20～25 | 6 | 79 分钟（约 53 分钟）+ 复习 |

> Day 3 原本只有链表和矩阵（约 120 分钟），区间专题挪到了这一天，因为它和链表一样不需要额外的前置知识。如果觉得量太大，可以把区间留到 Day 7 的复习时间里。

---

## Day 1：数组 + 位运算

| 笔记 | 代码 |
| --- | --- |
| [数组](notes/01-数组.md) · [位运算](notes/02-位运算.md) | `c01_array.py` · `c02_binary.py` |

- **题目**：1, 121, 217, 238, 53, 152, 153, 33, 15, 11 · 191, 338, 268, 190, 371
- **当天重点**：哈希表、双指针、Kadane、旋转数组二分；位运算的五个基本技巧
- **自测**：
  1. Two Sum 为什么可以只遍历一遍？
  2. 152 题为什么要同时维护最小积？
  3. 33 题中，怎样判断 mid 在哪一段、target 在不在有序的那一半？
  4. `n & (n-1)` 做了什么？异或为什么能找出缺失的数？

## Day 2：字符串

| 笔记 | 代码 |
| --- | --- |
| [字符串](notes/08-字符串.md) | `c08_string.py` |

- **题目**：3, 424, 76, 49, 20, 125, 5, 647, 271, 242
- **当天重点**：滑动窗口模板（3 → 424 → 76，难度递进）、频次计数、中心扩展
- **自测**：
  1. 424 题中窗口合法的条件是什么？为什么 `maxf` 可以只增不减？
  2. 76 题的 have/need 分别是什么意思？
  3. 回文的中心为什么有 2n-1 个？
  4. 271 题为什么不能只用分隔符？

## Day 3：链表 + 区间 + 矩阵

| 笔记 | 代码 |
| --- | --- |
| [链表](notes/06-链表.md) · [区间](notes/05-区间.md) · [矩阵](notes/07-矩阵.md) | `c06_linked_list.py` · `c05_interval.py` · `c07_matrix.py` |

- **题目**：206, 141, 21, 23, 19, 143 · 57, 56, 435, 252, 253 · 73, 54, 48, 79
- **当天重点**：哑结点、快慢指针；区间先排序；矩阵原地操作和回溯
- **自测**：
  1. 为什么快慢指针在有环时一定会相遇？
  2. 143 题由哪三个基本操作组成？
  3. 435 题重叠时为什么删掉终点更大的那个？
  4. 253 题的两种解法分别是什么？
  5. 73 题为什么要额外用一个变量记录第 0 行？

## Day 4：树（上）+ 堆

| 笔记 | 代码 |
| --- | --- |
| [树](notes/09-树.md)（第 58～64 集）· [堆](notes/10-堆.md) | `c09_tree.py` · `c10_heap.py` |

- **题目**：104, 100, 226, 124, 102, 297, 572 · 347, 295
- **当天重点**：递归的三种遍历；104 题的三种写法；124 题的"分叉"；堆和桶排序
- **自测**：
  1. 用递归 DFS、BFS、迭代 DFS 分别写出 104 题。
  2. 124 题中，递归函数返回的值和全局答案有什么区别？
  3. 297 题为什么要记录空结点？
  4. 347 题的桶排序为什么是 O(n)？295 题要维护哪两个条件？

## Day 5：树（下）+ 图（上）

| 笔记 | 代码 |
| --- | --- |
| [树](notes/09-树.md)（第 65～71 集）· [图](notes/04-图.md)（第 26～29 集） | `c09_tree.py` · `c04_graph.py` |

- **题目**：105, 98, 230, 235, 208, 211, 212 · 133, 207, 417, 200
- **当天重点**：BST 的三条性质；Trie 的实现；图的 DFS/BFS + visited、有向图找环
- **自测**：
  1. 98 题只比较父子结点为什么不对？
  2. 105 题中，左子树在前序和中序里分别是哪一段？
  3. 212 题为什么比对每个单词都做一次 79 题快？
  4. 207 题怎样判断有环？417 题的"反向思维"是什么？

## Day 6：图（下）+ DP（上）

| 笔记 | 代码 |
| --- | --- |
| [图](notes/04-图.md)（第 30～33 集）· [动态规划](notes/03-动态规划.md)（第 15～19 集） | `c04_graph.py` · `c03_dp.py` |

- **题目**：128, 269, 261, 323 · 70, 322, 300, 1143, 139
- **当天重点**：拓扑排序、无向图找环、并查集；DP 四步走
- **自测**：
  1. 128 题为什么是 O(n)？
  2. 269 题有哪两种不合法的情况？
  3. 并查集的两个优化分别是什么？
  4. 322 题为什么不能用贪心？用 `coins=[1,3,4,5]`、`amount=7` 举例。
  5. 1143 题字符相等和不相等时，分别从哪个格子转移过来？

## Day 7：DP（下）+ 总复习

| 笔记 | 代码 |
| --- | --- |
| [动态规划](notes/03-动态规划.md)（第 20～25 集）· [全系列总结](notes/11-全系列总结.md) | `c03_dp.py` · `python run_all.py` |

- **题目**：39, 198, 213, 91, 62, 55
- **当天重点**：回溯如何避免重复组合；打家劫舍的滚动变量；贪心
- **自测**：
  1. 39 题的决策树为什么只有两个分支？
  2. 213 题为什么要拆成两次 198 题？
  3. 55 题的贪心为什么是对的？
- **总复习（约 1.5 小时）**：
  1. 对照[全系列总结](notes/11-全系列总结.md)里的"看到什么，想到什么"表，逐行口述代表题的思路；
  2. 对照"易错点清单"，每条都回到代码里找到对应的那一行；
  3. 从前 6 天中**随机抽 5 道题**，每道限时 20 分钟，按 NeetCode 的流程讲出来：暴力解 → 优化 → 复杂度 → 代码。

---

## 7 天之后

- **第二遍**：Blind 75 刷第二遍时，**不看笔记直接做**。卡住超过 20 分钟的题标记出来，第三天再做一次。
- **扩展**：NeetCode 后来又整理了 **NeetCode 150**，在 Blind 75 的基础上增加了 75 道题，可以作为下一阶段的目标。
- **结合第一个系列**：Leetcode18 仓库里的《刷题套路系列》讲的是模板，遇到某个专题不熟时，可以回去看对应的那一集（对应关系见[全系列总结](notes/11-全系列总结.md#六和第一个系列的对应关系)）。


---

# 专题 1：数组 Array（第 1～10 集）

> 本专题的核心技巧：**哈希表**（用空间换查找速度）、**双指针 / 滑动窗口**、**前缀 / 后缀**、**Kadane（丢掉负的前缀）**、**旋转数组上的二分查找**。
> NeetCode 每道题的讲法几乎都一样：**先说暴力解，再找到可以优化的关键观察，然后画图推演，最后写代码**。面试时也建议照这个顺序讲。

| 集 | 题目 | 难度 | 关键技巧 | 时间 / 空间 |
| --- | --- | --- | --- | --- |
| 1 | [1. Two Sum 两数之和](https://leetcode.cn/problems/two-sum/) | Easy | 哈希表 值→下标 | O(n) / O(n) |
| 2 | [121. Best Time to Buy and Sell Stock](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/) | Easy | 双指针，左指针始终停在最低价 | O(n) / O(1) |
| 3 | [217. Contains Duplicate](https://leetcode.cn/problems/contains-duplicate/) | Easy | 哈希集合 | O(n) / O(n) |
| 4 | [238. Product of Array Except Self](https://leetcode.cn/problems/product-of-array-except-self/) | Medium | 前缀积 × 后缀积 | O(n) / O(1) |
| 5 | [53. Maximum Subarray](https://leetcode.cn/problems/maximum-subarray/) | Medium | Kadane：负的前缀直接丢掉 | O(n) / O(1) |
| 6 | [152. Maximum Product Subarray](https://leetcode.cn/problems/maximum-product-subarray/) | Medium | 同时维护最大积和最小积 | O(n) / O(1) |
| 7 | [153. Find Minimum in Rotated Sorted Array](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/) | Medium | 二分：判断 mid 在左段还是右段 | O(log n) / O(1) |
| 8 | [33. Search in Rotated Sorted Array](https://leetcode.cn/problems/search-in-rotated-sorted-array/) | Medium | 二分：先找有序的那一半 | O(log n) / O(1) |
| 9 | [15. 3Sum 三数之和](https://leetcode.cn/problems/3sum/) | Medium | 排序 + 固定一个数 + 相向双指针 | O(n²) / O(1) |
| 10 | [11. Container With Most Water](https://leetcode.cn/problems/container-with-most-water/) | Medium | 相向双指针，移动短板 | O(n) / O(1) |

---

## 第 1 集 · 1. Two Sum

**题意**：找出数组中和为 target 的两个数，返回它们的下标。题目保证恰好有一个解。

- **暴力**：枚举所有两两组合。对每个数，只需检查它**后面**的数，因为前面的组合已经检查过了。时间 O(n²)。
- **关键观察**：对于数 `n`，要找的另一个数**只能是 `target - n`**。所以问题变成"快速判断某个值是否出现过"，用哈希表就能 O(1) 完成。
- **一遍扫描的技巧**：不必先把所有数都存进哈希表。边遍历边处理：先查 `target - n` 在不在表里，**再**把 `n` 存进去。这样哈希表里永远只有"当前元素之前的元素"，自然不会把同一个元素用两次，也省去了处理边界情况的代码。

```python
# 哈希表：值 -> 下标。对每个数，先查 target - n 是否出现过，再把自己存进去
def two_sum(nums: List[int], target: int) -> List[int]:
    prev = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev:
            return [prev[diff], i]
        prev[n] = i
    return []
```

## 第 2 集 · 121. 买卖股票的最佳时机

**题意**：只能买卖一次，求最大利润。`[7,1,5,3,6,4]` 在 1 买入、6 卖出，利润为 5。

- **画折线图**：利润最大，就是找"最低点"和"它**之后**的最高点"。不能简单地用最大值减最小值，因为**时间只能往前走**，不能先卖后买。
- **双指针**：左指针 `l` 是买入日，右指针 `r` 是卖出日。
  - `prices[r] > prices[l]`：能赚钱，更新最大利润；
  - 否则说明找到了更低的价格，**把 `l` 直接挪到 `r`**，而不是只往右挪一格。NeetCode 在视频里先写成了 `l += 1`，后来自己指出这是个 bug：我们希望左指针始终停在**目前为止的最低价**上。

```python
# 双指针 / 滑动窗口：l 是买入日（始终指向目前最低价），r 是卖出日
def max_profit(prices: List[int]) -> int:
    l, best = 0, 0
    for r in range(1, len(prices)):
        if prices[r] > prices[l]:
            best = max(best, prices[r] - prices[l])
        else:
            l = r                      # 发现更低的价格：直接把买入日挪到这里
    return best
```

## 第 3 集 · 217. 存在重复元素

**题意**：数组中有没有出现至少两次的值？

NeetCode 讲了三种解法，体现了时间和空间的取舍：

| 解法 | 思路 | 时间 | 空间 |
| --- | --- | --- | --- |
| 暴力 | 每个数都和其余所有数比较 | O(n²) | O(1) |
| 排序 | 排序后重复元素一定**相邻**，比较相邻元素即可 | O(n log n) | O(1) |
| 哈希集合 | 加入集合之前先检查是否已经存在 | O(n) | O(n) |

```python
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
```

## 第 4 集 · 238. 除自身以外数组的乘积

**题意**：`answer[i]` 等于除 `nums[i]` 外其余所有数的乘积。要求 **O(n) 时间，不能用除法**。

- 如果能用除法，算出总乘积再除以 `nums[i]` 就行了。难点在于不能用除法。
- **关键观察**：除 `nums[i]` 以外的乘积 = **i 左边所有数的乘积（前缀积）× i 右边所有数的乘积（后缀积）**。
- **O(1) 额外空间的做法**（输出数组不算额外空间）：
  1. 从左往右扫，把前缀积直接写进 `res[i]`；
  2. 从右往左扫，用一个变量 `postfix` 记录后缀积，**乘到 `res[i]` 上**。注意不能直接覆盖，否则会丢掉第 1 步写进去的前缀积。

`[1,2,3,4]` 的前缀积是 `[1,1,2,6]`，后缀积是 `[24,12,4,1]`，对应相乘得到 `[24,12,8,6]`。

```python
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
```

## 第 5 集 · 53. 最大子数组和（Kadane 算法）

**题意**：找和最大的连续子数组，返回它的和。

- **暴力**：三层循环，枚举起点、终点，再求和，O(n³)；用累加省掉求和那层循环，O(n²)。
- **关键观察**：如果某段**前缀的和是负数**，它只会拖累后面的和，应该直接**丢掉**。
- 做法：维护当前和 `cur`，一旦变成负数就重置为 0，再加上当前数，同时更新最大值。
- 最大值的初值设为 `nums[0]` 而不是 0，因为数组可能全是负数。

```python
# 当前和一旦变成负数，它只会拖累后面 -> 丢掉（重置为 0）
def max_sub_array(nums: List[int]) -> int:
    best, cur = nums[0], 0
    for n in nums:
        if cur < 0:
            cur = 0
        cur += n
        best = max(best, cur)
    return best
```

## 第 6 集 · 152. 乘积最大子数组（DP）

**题意**：找乘积最大的连续子数组。

- 和 53 题的区别在于**负数**：一个很小的负数，乘上一个负数后会变成很大的正数。
- **关键观察**：只记录"以当前位置结尾的最大积"不够，还要同时记录**最小积**。因为最小积（负得最多的那个）乘上一个负数，可能翻身变成最大值。
- 每一步的候选值有三个：`n × 之前的最大积`、`n × 之前的最小积`，以及 `n` 本身（从当前位置重新开始）。
- **必须同时更新** `cur_max` 和 `cur_min`。Python 用元组同时赋值，避免用到已经被更新过的值。
- `0` 会把积清零，不需要单独处理，因为 `n` 本身也是候选值，相当于从下一个数重新开始。

```python
# 负数会让最小值翻身成最大值 -> 同时维护"以当前结尾的最大积和最小积"
def max_product(nums: List[int]) -> int:
    res = max(nums)
    cur_max = cur_min = 1
    for n in nums:
        candidates = (n * cur_max, n * cur_min, n)
        cur_max, cur_min = max(candidates), min(candidates)   # 必须同时更新
        res = max(res, cur_max)
    return res
```

## 第 7 集 · 153. 寻找旋转排序数组中的最小值

**题意**：一个升序数组被旋转过（比如 `[3,4,5,1,2]`），元素互不相同，要求 **O(log n)** 找出最小值。

- 题目要求 log n，而且数组原来是有序的，提示我们用**二分查找**。
- **关键观察**：旋转后的数组由两段升序序列组成，**左段的值都比右段大**，最小值就是右段的第一个元素。
  - 如果 `nums[l] < nums[r]`，说明当前区间已经整体有序，`nums[l]` 就是最小值，可以直接结束。
  - `nums[m] >= nums[l]`：m 在**左段**，最小值在 m 的右边，所以 `l = m + 1`；
  - 否则 m 在**右段**，最小值在 m 或 m 的左边，所以 `r = m - 1`，并且已经用 `res` 记下了 `nums[m]`。

```python
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
```

## 第 8 集 · 33. 搜索旋转排序数组

**题意**：在旋转排序数组里查找 target，找到返回下标，否则返回 -1，要求 O(log n)。

- 先和 153 题一样判断 **m 在左段还是右段**：`nums[l] <= nums[m]` 说明 m 在左段，`[l, m]` 这一半是有序的。
- 然后判断 **target 是否落在有序的那一半里**：
  - m 在左段：如果 `nums[l] <= target < nums[m]`，就去左边找，否则去右边找；
  - m 在右段：如果 `nums[m] < target <= nums[r]`，就去右边找，否则去左边找。
- NeetCode 强调：代码看着简单，但一定要**先画图**，把每种情况想清楚再写代码。

```python
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
```

## 第 9 集 · 15. 三数之和

**题意**：找出所有和为 0 且**不重复**的三元组。

- NeetCode 建议先做 1（两数之和）和 **167（两数之和 II，输入有序）**，做完这两道，三数之和就很直接了。
- **暴力**：三层循环 O(n³)，而且去重很麻烦。
- **做法**：
  1. **排序**：既方便用双指针，也方便去重；
  2. **固定第一个数 a**，剩下的问题就变成"在 a 右边的有序数组里找两个数，和为 -a"，用**相向双指针**解决；
  3. **去重**：a 和上一个数相同就跳过；找到一组解后，左指针跳过所有相同的值。
- 小优化：a > 0 时直接结束，因为后面的数都是正数，三数之和不可能为 0。

```python
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
```

## 第 10 集 · 11. 盛最多水的容器

**题意**：选两条线，与 x 轴构成容器，求最大面积。

- **暴力**：枚举所有左右两条线的组合，O(n²)。
- **关键观察**：面积 = 宽度 × **较短那条线的高度**，水会从短的那边漏出去。
- **双指针从两端开始**，因为一开始宽度最大。之后**每次移动较短的那一边**：移动较长的那一边，宽度变小而高度不会超过短板，面积只会更小；只有移动短板，才有可能找到更高的线。
- 两边一样高时，移动哪一边都可以。

```python
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
```

## 运行结果

运行 `python c01_array.py` 的实际输出：

```text
1    two_sum([2,7,11,15], 9) -> [0, 1]
121  max_profit([7,1,5,3,6,4]) -> 5 | [7,6,4,3,1] -> 0
217  contains_duplicate([1,2,3,1]) -> True | [1,2,3,4] -> False | 排序版 -> True
238  product_except_self([1,2,3,4]) -> [24, 12, 8, 6]
53   max_sub_array([-2,1,-3,4,-1,2,1,-5,4]) -> 6
152  max_product([2,3,-2,4]) -> 6 | [-2,3,-4] -> 24
153  find_min([3,4,5,1,2]) -> 1 | [4,5,6,7,0,1,2] -> 0
33   search([4,5,6,7,0,1,2], 0) -> 4 | target=3 -> -1
15   three_sum([-1,0,1,2,-1,-4]) -> [[-1, -1, 2], [-1, 0, 1]]
11   max_area([1,8,6,2,5,4,8,3,7]) -> 49
```

## 本专题要点
- "某个值是否出现过"、"补数在哪里"这类问题，用**哈希表**降到 O(n)。
- 求"连续"的最优值：53 题丢掉负的前缀，152 题同时维护最大值和最小值。
- 不能用除法时，考虑**前缀 × 后缀**。
- 要求 O(log n)，并且数组"原本有序"，考虑**二分查找**，关键是判断 mid 落在哪一段。
- 有序数组上找两个数，用**相向双指针**；三数之和 = 排序 + 固定一个数 + 两数之和 II。


---

# 专题 2：位运算 Binary（第 11～14 集 + 第 75 集）

> 第 75 集 Sum of Two Integers 在播放列表的最后，内容属于位运算，所以放在这个专题里一起讲。
> NeetCode 认为这类题适合用来**复习位运算的基本操作**：`&`（与）、`|`（或）、`^`（异或）、`>>` / `<<`（移位）。

## 位运算速查

| 操作 | 含义 | 常见用途 |
| --- | --- | --- |
| `n & 1` | 取最低位 | 判断奇偶，逐位统计 |
| `n >> 1` | 右移一位，相当于整除 2 | 逐位处理 |
| `1 << k` | 只有第 k 位是 1 | 设置某一位 |
| `n & (n - 1)` | 消掉最右边的那个 1 | 统计 1 的个数，判断是否为 2 的幂 |
| `a ^ a = 0`，`a ^ 0 = a` | 相同的数异或为 0 | 找出"只出现一次"或"缺失"的数 |
| `a ^ b` / `(a & b) << 1` | 不进位的加法 / 进位 | 不用加号做加法 |

| 集 | 题目 | 难度 | 关键技巧 | 时间 / 空间 |
| --- | --- | --- | --- | --- |
| 11 | [191. Number of 1 Bits](https://leetcode.cn/problems/number-of-1-bits/) | Easy | 逐位 `& 1`；或者 `n & (n-1)` | O(1) / O(1) |
| 12 | [338. Counting Bits](https://leetcode.cn/problems/counting-bits/) | Easy | DP：`dp[i] = 1 + dp[i - offset]` | O(n) / O(n) |
| 13 | [268. Missing Number](https://leetcode.cn/problems/missing-number/) | Easy | 异或 / 求和差 | O(n) / O(1) |
| 14 | [190. Reverse Bits](https://leetcode.cn/problems/reverse-bits/) | Easy | 取第 i 位，放到第 31-i 位 | O(1) / O(1) |
| 75 | [371. Sum of Two Integers](https://leetcode.cn/problems/sum-of-two-integers/) | Medium | 异或 + 进位，循环到没有进位 | O(1) / O(1) |

---

## 第 11 集 · 191. 位 1 的个数

**题意**：统计一个 32 位无符号整数的二进制里有多少个 1。

- **解法 1（逐位检查）**：`n & 1` 取出最低位（也可以写成 `n % 2`），累加后把 n 右移一位，直到 n 为 0。最多循环 32 次，所以是 O(1)。
- **解法 2（`n & (n-1)` 技巧）**：`n - 1` 会把最右边的 1 变成 0，并把它右边的 0 都变成 1。再和 n 做与运算，就**正好消掉了最右边的那个 1**。所以循环次数就是 1 的个数，不用看那些 0。
  - 例：`n = 1100`，`n-1 = 1011`，`n & (n-1) = 1000`，消掉了一个 1。
- 两种解法的大 O 相同，但第二种在 1 很少时更快。NeetCode 在视频里两种都讲了。

```python
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
```

## 第 12 集 · 338. 比特位计数（DP）

**题意**：返回数组 `ans`，其中 `ans[i]` 是 i（0 ≤ i ≤ n）的二进制里 1 的个数。

- **暴力**：对每个数都用 191 题的方法数一遍，O(n log n)。
- **关键观察**：把 0～8 的二进制写出来，会发现**重复的模式**：
  - 4～7 是 `1xx`，后两位正好是 0～3 的二进制，所以 `dp[4..7] = 1 + dp[0..3]`；
  - 8 是 `1000`，所以 `dp[8] = 1 + dp[0]`。
- 所以 `dp[i] = 1 + dp[i - offset]`，其中 **offset 是不超过 i 的最大的 2 的幂**，也就是 i 的最高有效位。遍历时，一旦 `offset * 2 == i`，就把 offset 更新成 i。
- 另一种常见写法：`dp[i] = dp[i >> 1] + (i & 1)`。去掉最低位后的数已经算过了，再加上最低位。

```python
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
```

## 第 13 集 · 268. 丢失的数字

**题意**：数组包含 `[0, n]` 中的 n 个**不同**的数，找出缺失的那个。

NeetCode 说这道 Easy 题有很多种解法，很值得学习：

| 解法 | 思路 | 时间 | 空间 |
| --- | --- | --- | --- |
| 排序 | 排序后逐个比较下标和值 | O(n log n) | O(1) |
| 哈希集合 | 把数组放进集合，逐个检查 0～n | O(n) | O(n) |
| **异或** | 把 0～n 和数组里的所有数全部异或，成对出现的都抵消成 0，最后剩下的就是缺失的数 | O(n) | O(1) |
| **求和差** | `sum(0..n) - sum(nums)` | O(n) | O(1) |

- 异或的原理：`a ^ a = 0`，`a ^ 0 = a`，而且异或满足交换律，顺序无关。
- 求和差的写法：把 `res` 初值设为 n，然后边遍历边做 `res += i - nums[i]`，就不需要单独再算一次总和。

```python
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
```

## 第 14 集 · 190. 颠倒二进制位

**题意**：把一个 32 位无符号整数的二进制位完全颠倒。

- 依次取出第 i 位：`(n >> i) & 1`；
- 把它放到第 `31 - i` 位上：`res |= bit << (31 - i)`。
- 固定循环 32 次，时间和空间都是 O(1)。NeetCode 认为这是一道复习位运算的好题。

```python
# 依次取出第 i 位，放到第 31 - i 位上
def reverse_bits(n: int) -> int:
    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        res |= bit << (31 - i)
    return res
```

## 第 75 集 · 371. 两整数之和

**题意**：不使用 `+` 和 `-` 运算符，计算两个整数的和。

- **按位相加的规律**：
  - `a ^ b`：每一位**不考虑进位**的和（1+1=0，1+0=1，0+0=0）；
  - `(a & b) << 1`：**进位**，只有两位都是 1 时才产生进位，进到左边一位。
- 把"不进位的和"与"进位"再相加，又是同样的问题，所以**循环到进位为 0 为止**。
- **为什么视频用 Java 写**：Python 的整数没有位数上限，负数的进位会一直往左移，循环永远不会结束。Python 版需要用 `0xFFFFFFFF` 掩码**模拟 32 位整数**，最后再把结果还原成有符号数。代码里已经处理好了。

```python
# 异或 = 不进位的加法；与运算再左移一位 = 进位。反复相加直到没有进位
# Python 的整数没有位数上限，要用 32 位掩码模拟（视频里用 Java 写，就是因为这个）
def get_sum(a: int, b: int) -> int:
    mask = 0xFFFFFFFF
    while b & mask:
        a, b = a ^ b, (a & b) << 1
    a &= mask
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)   # 还原成有符号数
```

## 运行结果

运行 `python c02_binary.py` 的实际输出：

```text
191 hamming_weight(0b1011) -> 3 | n&(n-1) 版 -> 3
191 hamming_weight(0b10000000) -> 1
338 count_bits(5) -> [0, 1, 1, 2, 1, 2] | 移位版 -> [0, 1, 1, 2, 1, 2]
338 count_bits(8) -> [0, 1, 1, 2, 1, 2, 2, 3, 1]
268 missing_number([3,0,1]) -> 2 | [9,6,4,2,3,5,7,0,1] -> 8 | 求和版 -> 2
190 reverse_bits(43261596) -> 964176192 (二进制 00111001011110000010100101000000)
371 get_sum(1, 2) -> 3 | get_sum(2, 3) -> 5 | get_sum(-2, 3) -> 1 | get_sum(-5, -7) -> -12
```

## 本专题要点
- 逐位处理用 `(n >> i) & 1`，消掉最右边的 1 用 `n & (n-1)`。
- **异或**能让成对的数互相抵消，适合"只出现一次"和"缺失的数"这类题。
- 338 题是"位运算 + DP"：利用最高位（或最低位）把问题拆成已经算过的子问题。
- 用 Python 做位运算时，要注意它的整数**没有位数上限**，必要时用掩码模拟 32 位。


---

# 专题 3：动态规划 Dynamic Programming（第 15～25 集）

> NeetCode 讲 DP 的固定套路是：
> 1. **画决策树**，写出暴力递归，看清楚哪些子问题被重复计算；
> 2. **加缓存（memoization）**，变成 Top-down DP；
> 3. **倒过来从最小的子问题开始填表**，变成 Bottom-up DP，再观察能不能**只保留最近几个状态**，把空间降到 O(1)。
>
> 他的 Bottom-up 写法经常**从数组末尾往前算**，`dp[i]` 表示"从 i 开始到结尾"的答案。这和中文教材里常见的"前 i 个"方向相反，但思路完全一样。

| 集 | 题目 | 难度 | 状态定义 | 递推 / 技巧 | 时间 / 空间 |
| --- | --- | --- | --- | --- | --- |
| 15 | [70. Climbing Stairs](https://leetcode.cn/problems/climbing-stairs/) | Easy | `dp[i]` = 从第 i 级到顶的方法数 | `dp[i] = dp[i+1] + dp[i+2]`（斐波那契） | O(n) / O(1) |
| 16 | [322. Coin Change](https://leetcode.cn/problems/coin-change/) | Medium | `dp[a]` = 凑出 a 的最少硬币数 | `1 + min(dp[a-c])` | O(amount·k) / O(amount) |
| 17 | [300. Longest Increasing Subsequence](https://leetcode.cn/problems/longest-increasing-subsequence/) | Medium | `LIS[i]` = 以 i 开头的 LIS 长度 | `1 + max(LIS[j])`，j>i 且更大 | O(n²) / O(n) |
| 18 | [1143. Longest Common Subsequence](https://leetcode.cn/problems/longest-common-subsequence/) | Medium | `dp[i][j]` = `text1[i:]` 和 `text2[j:]` 的 LCS | 相等：1+右下；不等：max(右, 下) | O(mn) / O(mn) |
| 19 | [139. Word Break](https://leetcode.cn/problems/word-break/) | Medium | `dp[i]` = `s[i:]` 能否拆分 | 某个单词匹配 `s[i:]` 开头，且 `dp[i+len]` 为真 | O(n·m·k) / O(n) |
| 20 | [39. Combination Sum](https://leetcode.cn/problems/combination-sum/) | Medium | 回溯：(下标 i, 当前组合, 当前和) | "继续用 i" 或 "不再用 i" 两个分支 | O(2^t) / O(t) |
| 21 | [198. House Robber](https://leetcode.cn/problems/house-robber/) | Medium | 偷到当前房子为止的最大金额 | `max(n + rob1, rob2)` | O(n) / O(1) |
| 22 | [213. House Robber II](https://leetcode.cn/problems/house-robber-ii/) | Medium | 同上 | 去掉首或去掉尾，各算一次 198 | O(n) / O(1) |
| 23 | [91. Decode Ways](https://leetcode.cn/problems/decode-ways/) | Medium | `dp[i]` = `s[i:]` 的解码数 | 一位（非 0）+ 两位（10～26） | O(n) / O(n) |
| 24 | [62. Unique Paths](https://leetcode.cn/problems/unique-paths/) | Medium | 每格到终点的路径数 | 右边 + 下边，只保留一行 | O(mn) / O(n) |
| 25 | [55. Jump Game](https://leetcode.cn/problems/jump-game/) | Medium | 贪心：终点往前挪 | 能跳到终点就把终点挪到自己 | O(n) / O(1) |

---

## 第 15 集 · 70. 爬楼梯

**题意**：每次爬 1 级或 2 级，爬到第 n 级有多少种方法？

- **决策树**：每一步都分出"走 1 级"和"走 2 级"两个分支，暴力递归是 O(2ⁿ)。
- 画出来会发现**大量重复的子问题**，比如"从第 3 级出发有几种走法"会被算很多次。加缓存后变成 O(n)。
- **Bottom-up**：从顶部往下算，最后两级的答案都是 1，之后每一级 = 上一级 + 上上一级，**就是斐波那契数列**。只需要两个变量 `one`、`two`，空间 O(1)。

```python
# 从终点倒推：dp[i] = dp[i+1] + dp[i+2]，本质就是斐波那契。只需两个变量
def climb_stairs(n: int) -> int:
    one, two = 1, 1                      # 视频里从底部往回算：最后两级都只有 1 种
    for _ in range(n - 1):
        one, two = one + two, one
    return one
```

## 第 16 集 · 322. 零钱兑换

**题意**：用最少的硬币凑出 amount，每种硬币可以无限使用，凑不出返回 -1。

- **贪心不对**：NeetCode 举了反例 `coins = [1,3,4,5]`，`amount = 7`。贪心先拿 5，再拿 1+1，共 3 枚；最优解是 3+4，只要 2 枚。
- **决策树**：每一步都尝试每一种硬币，剩下的金额继续递归。剩余金额相同的子问题会重复出现，所以用 DP。
- **Bottom-up**：`dp[0] = 0`，然后从小到大算，`dp[a] = min(dp[a], 1 + dp[a - c])`。
- 初值设成 `amount + 1`，相当于"无穷大"，因为最多也只需要 amount 枚 1 元硬币。最后还是 `amount + 1` 就说明凑不出来，返回 -1。

```python
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
```

## 第 17 集 · 300. 最长递增子序列

**题意**：求最长严格递增**子序列**的长度。子序列可以不连续，但顺序不能变。

- **暴力**：每个元素选或不选，共 2ⁿ 种子序列。
- **DP（从后往前）**：`LIS[i]` 表示**以 i 开头**的最长递增子序列长度。
  - 最后一个元素的 `LIS` 是 1；
  - 对每个 i，看它右边所有比它大的 `nums[j]`：`LIS[i] = max(LIS[i], 1 + LIS[j])`。
  - 答案是整个 `LIS` 数组的最大值，因为最长子序列不一定从第 0 个元素开始。
- 时间 O(n²)。代码中额外附上了 **O(n log n)** 的"贪心 + 二分"解法：维护每个长度的递增子序列的最小结尾。视频里没讲，面试时提出来可以加分。

```python
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
```

## 第 18 集 · 1143. 最长公共子序列

**题意**：求两个字符串的最长公共子序列的长度。

- **画二维表**：行是 text1，列是 text2，多开一行一列作为边界（值为 0）。
- `dp[i][j]` 表示 `text1[i:]` 和 `text2[j:]` 的 LCS，**从右下角往左上角填**：
  - 字符相等：两个字符都用掉，答案是 `1 + 右下角`，即 `1 + dp[i+1][j+1]`；
  - 不相等：丢掉其中一个，取 **右边** `dp[i][j+1]` 和 **下边** `dp[i+1][j]` 中较大的。
- 答案在左上角 `dp[0][0]`。

```python
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
```

## 第 19 集 · 139. 单词拆分

**题意**：字符串 s 能否被拆分成字典中的单词？单词可以重复使用。

- **暴力想法**：从每个位置开始，尝试所有可能的前缀。NeetCode 的做法是**反过来遍历字典里的单词**，检查哪个单词恰好匹配 `s` 当前位置开头的子串。字典里的单词通常不多，而且都比较短。
- **DP（从后往前）**：`dp[i]` 表示 `s[i:]` 能否被拆分。
  - `dp[len(s)] = True`：空串可以拆分，这是 base case；
  - 对每个 i，如果某个单词 `w` 满足 `s[i : i+len(w)] == w`，并且 `dp[i + len(w)]` 为真，那么 `dp[i]` 为真。
- 例：`s = "neetcode"`。`dp[4]` 为真，因为 `"code"` 匹配，且 `dp[8]` 为真；`dp[0]` 也为真，因为 `"neet"` 匹配，且 `dp[4]` 为真。

```python
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
```

## 第 20 集 · 39. 组合总和（回溯）

**题意**：从 candidates 中选数（可以重复选），找出所有和为 target 的组合，组合不能重复。

- **朴素的决策树**：每一步都尝试所有数，会产生重复组合，比如 `[2,2,3]` 和 `[2,3,2]`。
- **NeetCode 的去重方法**：每个结点只分**两个分支**：
  - **左分支**：继续使用 `candidates[i]`（下标不变）；
  - **右分支**：**以后再也不用** `candidates[i]`（下标 i+1）。
  这样每个组合只会以一种方式出现，从根本上避免了重复。
- base case：和等于 target 就记录答案（要**复制**当前组合）；下标越界或者和超过 target，就返回。
- 时间复杂度约为 O(2^t)，t 是 target 的大小，因为树的高度最多为 t。

```python
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
```

## 第 21 集 · 198. 打家劫舍

**题意**：不能偷相邻的两间房，求最多能偷多少钱。

- **决策**：对第 i 间房，要么偷（加上**隔一间之前**的最优值），要么不偷（沿用**上一间**的最优值）。
- 状态只依赖前两个值，所以用两个变量 `rob1`、`rob2` 滚动更新：
  - `new = max(n + rob1, rob2)`；
  - 然后 `rob1, rob2 = rob2, new`。
- 时间 O(n)，空间 O(1)。

```python
# rob = max(当前房子 + 隔一间之前的最优, 上一间的最优)，只需两个变量
def rob(nums: List[int]) -> int:
    rob1, rob2 = 0, 0                    # [rob1, rob2, n, n+1, ...]
    for n in nums:
        rob1, rob2 = rob2, max(n + rob1, rob2)
    return rob2
```

## 第 22 集 · 213. 打家劫舍 II

**题意**：房子**围成一圈**，第一间和最后一间也算相邻。

- **关键观察**：第一间和最后一间不能同时偷。所以分两种情况：
  - 去掉第一间，对 `nums[1:]` 做一次 198 题；
  - 去掉最后一间，对 `nums[:-1]` 做一次 198 题；
  - 取两者的较大值。
- **边界情况**：只有一间房时，两个子数组都是空的，所以要把 `nums[0]` 也放进 `max` 里。
- 直接复用 198 题的函数作为辅助函数。

```python
# 首尾不能同时偷 -> 去掉第一间算一次，去掉最后一间算一次，取较大值（只有一间房要单独处理）
def rob_circle(nums: List[int]) -> int:
    return max(nums[0], rob(nums[1:]), rob(nums[:-1]))
```

## 第 23 集 · 91. 解码方法

**题意**：`'A'~'Z'` 编码为 `"1"~"26"`，求数字串有多少种解码方法。

- **决策树**：每一步可以取 1 位数字，也可以取 2 位数字。
  - 取 1 位：这一位不能是 `'0'`；
  - 取 2 位：必须在 10～26 之间，即第一位是 `'1'`，或者第一位是 `'2'` 且第二位在 `'0'~'6'` 之间。
- **DP（从后往前）**：`dp[len(s)] = 1`（空串有 1 种解码方法），然后：
  - `s[i] == '0'`：`dp[i] = 0`，以 0 开头的串无法解码；
  - 否则 `dp[i] = dp[i+1]`，再加上能取两位时的 `dp[i+2]`。

```python
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
```

## 第 24 集 · 62. 不同路径

**题意**：从 m×n 网格的左上角走到右下角，只能向右或向下走，有多少条路径？

- **从终点倒推**：最后一行和最后一列的每个格子都只有 1 条路径；其他格子的路径数 = **右边格子 + 下边格子**。
- **只保留一行**：计算当前行只需要用到下面那一行，所以空间是 O(n)。
- 补充：这道题也可以用组合数直接算出答案 C(m+n-2, m-1)，因为一共要走 m-1 步向下、n-1 步向右，只是选择哪几步向下。

```python
# 每个格子的路径数 = 右边 + 下边。只需保留一行
def unique_paths(m: int, n: int) -> int:
    row = [1] * n                        # 最底下一行全是 1
    for _ in range(m - 1):
        new_row = [1] * n
        for j in range(n - 2, -1, -1):
            new_row[j] = new_row[j + 1] + row[j]
        row = new_row
    return row[0]
```

## 第 25 集 · 55. 跳跃游戏（贪心）

**题意**：`nums[i]` 表示在位置 i 最多能跳几步，判断能否跳到最后一个位置。

- **DP 解法**：判断每个位置能否到达终点，O(n²)。
- **贪心解法（NeetCode 推荐）**：把**终点 goal 从最后一个位置往前挪**。
  - 从后往前遍历，如果 `i + nums[i] >= goal`，说明从 i 能跳到 goal，那么 i 就成了新的终点；
  - 最后判断 goal 是否挪到了 0。
- 时间 O(n)，空间 O(1)。

```python
# 把"终点"从最后往前挪：如果从 i 能跳到当前终点，那 i 就成了新的终点
def can_jump(nums: List[int]) -> bool:
    goal = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0
```

## 运行结果

运行 `python c03_dp.py` 的实际输出：

```text
70   climb_stairs(2), (3), (5) -> 2 3 8
322  coin_change([1,2,5], 11) -> 3 | ([2], 3) -> -1 | ([1,3,4,5], 7) -> 2
300  length_of_lis([10,9,2,5,3,7,101,18]) -> 4 | O(n log n) 版 -> 4
1143 longest_common_subsequence('abcde', 'ace') -> 3
139  word_break('neetcode', ['neet','code']) -> True | ('catsandog', [cats,dog,sand,and,cat]) -> False
39   combination_sum([2,3,6,7], 7) -> [[2, 2, 3], [7]]
198  rob([1,2,3,1]) -> 4 | rob([2,7,9,3,1]) -> 12
213  rob_circle([2,3,2]) -> 3 | [1,2,3,1] -> 4 | [1] -> 1
91   num_decodings('12'), ('226'), ('06') -> 2 3 0
62   unique_paths(3, 7) -> 28 | (3, 2) -> 3
55   can_jump([2,3,1,1,4]) -> True | [3,2,1,0,4] -> False
```

## 本专题要点
- DP 四步走：**画决策树 → 加缓存 → 倒过来填表 → 只保留需要的状态**。
- 状态通常是"从 i 开始"（NeetCode 的写法）或者"前 i 个"，两种写法本质相同。
- 先用反例检查贪心对不对，比如 322 题；能用贪心的题（比如 55 题）通常比 DP 更快。
- 打家劫舍、爬楼梯这类只依赖前两个状态的题，用两个变量就能把空间降到 O(1)。
- 组合类题目要避免重复：每个结点只分"继续用"和"不再用"两个分支。


---

# 专题 4：图 Graph（第 26～33 集）

> 图题的通用步骤：
> 1. **建图**：通常是**邻接表**（结点 → 邻居列表）。网格题不用建图，上下左右四个格子就是邻居。
> 2. **遍历**：DFS 或 BFS，用 **visited 集合**防止在环里死循环。
> 3. 按题意在遍历中**做事**：复制结点、检测环、计数、记录结果……
>
> 269、261、323 三道是 **LeetCode 会员题**。视频是在 LintCode 上讲的同一道题，代码中给出了完整解法和测试。

| 集 | 题目 | 难度 | 关键技巧 | 时间 / 空间 |
| --- | --- | --- | --- | --- |
| 26 | [133. Clone Graph](https://leetcode.cn/problems/clone-graph/) | Medium | DFS + 哈希表 旧结点→新结点 | O(V+E) / O(V) |
| 27 | [207. Course Schedule](https://leetcode.cn/problems/course-schedule/) | Medium | 邻接表 + DFS 找环 | O(V+E) / O(V+E) |
| 28 | [417. Pacific Atlantic Water Flow](https://leetcode.cn/problems/pacific-atlantic-water-flow/) | Medium | 反向思维：从海边往高处走，两个集合取交集 | O(mn) / O(mn) |
| 29 | [200. Number of Islands](https://leetcode.cn/problems/number-of-islands/) | Medium | 遇到新的 1 就计数，BFS 标记整座岛 | O(mn) / O(mn) |
| 30 | [128. Longest Consecutive Sequence](https://leetcode.cn/problems/longest-consecutive-sequence/) | Medium | 哈希集合，只从"序列起点"开始数 | O(n) / O(n) |
| 31 | [269. Alien Dictionary](https://leetcode.cn/problems/alien-dictionary/)（会员） | Hard | 比较相邻单词建图 + 拓扑排序 | O(总字符数) / O(1) |
| 32 | [261. Graph Valid Tree](https://leetcode.cn/problems/graph-valid-tree/)（会员） | Medium | 无环 + 连通；无向图要记住父结点 | O(V+E) / O(V+E) |
| 33 | [323. Number of Connected Components](https://leetcode.cn/problems/number-of-connected-components-in-an-undirected-graph/)（会员） | Medium | 并查集：每合并一次，分量数减 1 | O(E·α(V)) / O(V) |

---

## 第 26 集 · 133. 克隆图

**题意**：给出无向连通图中的一个结点，返回整张图的**深拷贝**。

- **难点**：图里有环，比如 1 的邻居有 2，2 的邻居又有 1。如果直接递归复制，会无限循环下去。
- **哈希表 `old_to_new`**：记录"旧结点 → 新结点"的对应关系。
  - DFS 到一个结点，先查表：已经复制过，就**直接返回那个副本**；
  - 否则新建副本并**立刻放进表里**，再递归复制它的所有邻居，把结果加入副本的邻居列表。
- 哈希表同时起到了 visited 集合的作用。

```python
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# DFS + 哈希表 old -> new：先建结点再递归连邻居，表里有就直接返回（防止环导致死循环）
def clone_graph(node):
    old_to_new = {}

    def dfs(node):
        if node in old_to_new:
            return old_to_new[node]
        copy = Node(node.val)
        old_to_new[node] = copy
        for nb in node.neighbors:
            copy.neighbors.append(dfs(nb))
        return copy

    return dfs(node) if node else None
```

## 第 27 集 · 207. 课程表

**题意**：`[a, b]` 表示修 a 之前必须先修 b，问能不能修完所有课。

- **本质**：先修关系构成一张有向图，**有环就修不完**，比如 a 依赖 b，b 又依赖 a。
- **建邻接表**：课程 → 它的先修课列表。
- **DFS 找环**：用 `visiting` 集合记录**当前 DFS 路径**上的课程。
  - 在当前路径上再次遇到同一门课，说明有环，返回 False；
  - 没有先修课的课程，一定能修完，返回 True；
  - 一门课的所有先修课都能修完，它就能修完。此时**把它的先修列表清空**，以后再访问到它就直接返回 True，避免重复计算。
- 图可能不连通，所以要对**每门课**都调用一次 DFS。

```python
# 邻接表 course -> 先修课；DFS 判断有没有环。visiting 集合 = 当前路径
# 某门课确认能修完后，把它的先修列表清空，下次访问直接返回 True（剪枝）
def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    pre_map = {i: [] for i in range(num_courses)}
    for crs, pre in prerequisites:
        pre_map[crs].append(pre)
    visiting = set()

    def dfs(crs):
        if crs in visiting:              # 在当前路径上又遇到自己 -> 有环
            return False
        if pre_map[crs] == []:           # 没有先修课（或已确认能修完）
            return True
        visiting.add(crs)
        for pre in pre_map[crs]:
            if not dfs(pre):
                return False
        visiting.remove(crs)
        pre_map[crs] = []
        return True

    return all(dfs(c) for c in range(num_courses))
```

## 第 28 集 · 417. 太平洋大西洋水流问题

**题意**：水只能从高处流向**相同或更低**的相邻格子。左边、上边挨着太平洋，右边、下边挨着大西洋。找出能同时流进两个大洋的格子。

- **暴力**：从每个格子出发做一次 DFS，看能不能同时到达两片海洋。最坏 O((mn)²)。
- **反向思维**：从**海洋边界出发，往"更高或一样高"的地方走**。能走到的格子，就能流进这片海。
  - 从第一行和第一列出发，得到太平洋集合 `pac`；
  - 从最后一行和最后一列出发，得到大西洋集合 `atl`；
  - 两个集合的**交集**就是答案。
- 每个格子在每个集合里最多访问一次，时间 O(mn)。

```python
# 反向思维：从海洋边界出发"往高处爬"，能到的格子就能流进这片海；两个集合取交集
def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    rows, cols = len(heights), len(heights[0])
    pac, atl = set(), set()

    def dfs(r, c, visit, prev_height):
        if ((r, c) in visit or r < 0 or c < 0 or r == rows or c == cols
                or heights[r][c] < prev_height):
            return
        visit.add((r, c))
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc, visit, heights[r][c])

    for c in range(cols):
        dfs(0, c, pac, heights[0][c])                  # 第一行 -> 太平洋
        dfs(rows - 1, c, atl, heights[rows - 1][c])    # 最后一行 -> 大西洋
    for r in range(rows):
        dfs(r, 0, pac, heights[r][0])                  # 第一列 -> 太平洋
        dfs(r, cols - 1, atl, heights[r][cols - 1])    # 最后一列 -> 大西洋
    return sorted([r, c] for r, c in pac & atl)
```

## 第 29 集 · 200. 岛屿数量

**题意**：网格中，上下左右相连的 `'1'` 组成一座岛，求岛屿数量。

- 遍历每个格子：遇到一个**还没访问过的 `'1'`**，岛屿数加 1，然后用 **BFS**（视频的写法，DFS 也可以）把与它相连的整座岛都标记为已访问。
- 之后再扫到这座岛上的其他格子时，因为已经访问过，就不会重复计数。
- BFS 的队列用 `deque`，邻居必须在网格内、是 `'1'`，并且没有访问过。

```python
# 遇到一个没访问过的 '1' 就计数 +1，并用 BFS 把整座岛标记为已访问（视频里用 BFS）
def num_islands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visit, islands = set(), 0

    def bfs(r, c):
        q = deque([(r, c)])
        visit.add((r, c))
        while q:
            row, col = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1"
                        and (nr, nc) not in visit):
                    q.append((nr, nc))
                    visit.add((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visit:
                bfs(r, c)
                islands += 1
    return islands
```

## 第 30 集 · 128. 最长连续序列

**题意**：找出数字连续的最长序列的长度（不要求在原数组中连续），要求 O(n)。

- **排序**是 O(n log n)，不满足要求。
- **关键观察**：在数轴上画出来，每个连续序列都有一个**起点**，起点的特征是 **`n - 1` 不在数组里**。
- 把所有数放进集合，对每个**起点**一直往后数 `n+1`、`n+2`……，记录最长的长度。
- 为什么是 O(n)：只有起点才会往后数，所以每个数最多被"数到"一次。

```python
# 放进 set；只有 n-1 不在集合里时，n 才是一个序列的"起点"，从起点往后数
def longest_consecutive(nums: List[int]) -> int:
    num_set = set(nums)
    longest = 0
    for n in num_set:
        if n - 1 not in num_set:
            length = 1
            while n + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest
```

## 第 31 集 · 269. 火星词典（Hard，会员题）

**题意**：给出按外星字母表排好序的单词列表，推出字母的顺序。不合法时返回空串。

- **建图**：比较**相邻的两个单词**，找到第一个不同的字符 `c1 != c2`，得到一条边 `c1 → c2`，表示 c1 排在 c2 前面。只看第一个不同的字符，后面的字符不提供任何信息。
- **不合法的情况**：
  - 前一个单词更长，而且**后一个单词是它的前缀**，比如 `"abc"` 排在 `"ab"` 前面；
  - 图中**有环**，比如 `["z","x","z"]` 会同时得到 z→x 和 x→z。
- **拓扑排序（后序 DFS）**：`visit[c] = True` 表示 c 在当前路径上，`False` 表示已经处理完。一个字符的所有后继都加入结果之后，再加入它自己。最后把结果**反转**，就是字母顺序。
- 示例 `["wrt","wrf","er","ett","rftt"]` 的答案是 `"wertf"`。

```python
# 相邻两个单词的第一个不同字符给出一条边 c1 -> c2；前缀更长却排在前面 -> 不合法
# 后序 DFS + 环检测，结果反转
def alien_order(words: List[str]) -> str:
    adj = {c: set() for w in words for c in w}
    for w1, w2 in zip(words, words[1:]):
        min_len = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""                    # 例如 "abc" 排在 "ab" 前面
        for j in range(min_len):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break
    visit = {}                           # False = 已访问（不在当前路径上）；True = 在当前路径上
    res = []

    def dfs(c):
        if c in visit:
            return visit[c]              # True 说明在当前路径上 -> 有环
        visit[c] = True
        for nb in adj[c]:
            if dfs(nb):
                return True
        visit[c] = False
        res.append(c)                    # 后序：所有后继都加入后才加入自己
        return False

    for c in sorted(adj):                # 排序只是为了输出稳定
        if dfs(c):
            return ""
    return "".join(reversed(res))
```

## 第 32 集 · 261. 以图判树（会员题）

**题意**：n 个结点和一些无向边，判断它们能否构成一棵树。

- **树的两个条件**：**无环**，并且**连通**（从任意一个点能走到所有点）。
- **无向图找环的坑**：A—B 这条边，从 A 走到 B 之后，B 的邻居里又有 A，会被误认为是环。所以 DFS 时要**记住从哪个结点过来（prev）**，跳过它。
- 从 0 出发 DFS：没有发现环，并且访问到的结点数等于 n，就是一棵树。
- 补充：树一定有 **n-1 条边**，可以先用这一点快速排除。

```python
# 是树 <=> 无环 且 连通。无向图 DFS 时要记住"从哪来的"，避免把父结点当成环
def valid_tree(n: int, edges: List[List[int]]) -> bool:
    if not n:
        return True
    adj = {i: [] for i in range(n)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    visit = set()

    def dfs(i, prev):
        if i in visit:
            return False                 # 不是从父结点回来却又见到 -> 有环
        visit.add(i)
        for j in adj[i]:
            if j == prev:
                continue
            if not dfs(j, i):
                return False
        return True

    return dfs(0, -1) and len(visit) == n   # 无环 + 所有点都访问到（连通）
```

## 第 33 集 · 323. 无向图中连通分量的数目（并查集，会员题）

**题意**：n 个结点和一些无向边，求连通分量的个数。

- DFS 也可以做，但 NeetCode 用这道题讲了**并查集（Union-Find）**：
  - 一开始每个结点都是自己的父结点，共 n 个分量；
  - 对每条边执行 `union`：如果两个端点的**根**不同，就合并，分量数减 1；根相同说明已经连通，什么都不做；
  - `find`：沿着父指针找到根，同时做**路径压缩**（`par[x] = par[par[x]]`），让树变矮；
  - **按秩合并**：把小树挂到大树下面，同样是为了让树保持矮。
- 两个优化一起用，`find` 几乎是 O(1)。

```python
# 初始 n 个分量；每成功合并一次，分量数 -1。按秩合并 + 路径压缩
def count_components(n: int, edges: List[List[int]]) -> int:
    par = list(range(n))
    rank = [1] * n

    def find(x):
        while x != par[x]:
            par[x] = par[par[x]]         # 路径压缩
            x = par[x]
        return x

    def union(a, b):
        p1, p2 = find(a), find(b)
        if p1 == p2:
            return 0
        if rank[p2] > rank[p1]:
            p1, p2 = p2, p1
        par[p2] = p1
        rank[p1] += rank[p2]
        return 1

    res = n
    for a, b in edges:
        res -= union(a, b)
    return res
```

## 运行结果

运行 `python c04_graph.py` 的实际输出：

```text
133  clone_graph(四个结点的环) -> 新结点 1 的邻居 [2, 4] | 是新对象: True
207  can_finish(2, [[1,0]]) -> True | (2, [[1,0],[0,1]]) -> False
417  pacific_atlantic(示例) -> [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
200  num_islands(示例2) -> 3
128  longest_consecutive([100,4,200,1,3,2]) -> 4
269  alien_order(['wrt','wrf','er','ett','rftt']) -> wertf | ['z','x','z'] -> '' | ['abc','ab'] -> ''
261  valid_tree(5, [[0,1],[0,2],[0,3],[1,4]]) -> True | 有环 -> False
323  count_components(5, [[0,1],[1,2],[3,4]]) -> 2
```

## 本专题要点
- 图可能有环，一定要用 **visited**（或者旧→新的哈希表）防止重复访问。
- **有向图找环**：记录"当前路径"（`visiting`）。**无向图找环**：记录"从哪来的"（`prev`）。
- **反向思维**：从目标（海洋）出发往回找，比从每个起点出发快得多（417 题）。
- 连通块计数：遇到新起点就计数，然后把整块标记掉（200 题）；或者用并查集（323 题）。
- 拓扑排序 = 后序 DFS 再反转，或者用 BFS（Kahn 算法，按入度为 0 的顺序出队）。


---

# 专题 5：区间 Interval（第 34～38 集）

> 区间题的万能第一步：**按起点排序**。排序之后，只需要比较"当前区间"和"上一个区间"。
> 两个区间 `[a, b]` 和 `[c, d]`（a ≤ c）**重叠**的条件是 `c < b`（端点相接是否算重叠，要看题目）。
> 252、253 是 **LeetCode 会员题**，视频在 LintCode 上讲解。

| 集 | 题目 | 难度 | 关键技巧 | 时间 / 空间 |
| --- | --- | --- | --- | --- |
| 34 | [57. Insert Interval](https://leetcode.cn/problems/insert-interval/) | Medium | 三种情况：在左边 / 在右边 / 重叠就合并 | O(n) / O(n) |
| 35 | [56. Merge Intervals](https://leetcode.cn/problems/merge-intervals/) | Medium | 排序后与上一个区间比较，终点取 max | O(n log n) / O(n) |
| 36 | [435. Non-overlapping Intervals](https://leetcode.cn/problems/non-overlapping-intervals/) | Medium | 贪心：重叠时删掉终点更大的 | O(n log n) / O(1) |
| 37 | [252. Meeting Rooms](https://leetcode.cn/problems/meeting-rooms/)（会员） | Easy | 排序后检查相邻会议是否重叠 | O(n log n) / O(1) |
| 38 | [253. Meeting Rooms II](https://leetcode.cn/problems/meeting-rooms-ii/)（会员） | Medium | 开始、结束时间分别排序 + 双指针 | O(n log n) / O(n) |

---

## 第 34 集 · 57. 插入区间

**题意**：区间列表已经按起点排好序，并且互不重叠。插入一个新区间，必要时合并。

遍历每个区间 `cur`，和新区间 `new` 比较，有三种情况：
1. **`new` 完全在 `cur` 左边**（`new.end < cur.start`）：先加入 `new`，再把剩下的区间**原样接上**，直接返回，因为后面不可能再重叠了；
2. **`new` 完全在 `cur` 右边**（`new.start > cur.end`）：`cur` 原样加入结果；
3. **重叠**：把两者合并成更大的新区间 `[min(起点), max(终点)]`，**先不加入结果**，因为它可能还会和后面的区间重叠。

循环结束后，如果 `new` 还没加入（它在最右边，或者一直在合并），就把它加到最后。

```python
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
```

## 第 35 集 · 56. 合并区间

**题意**：合并所有重叠的区间。

- **按起点排序**，这样可以重叠的区间一定是挨在一起的。
- 遍历：当前起点 ≤ 结果中最后一个区间的终点，说明重叠，把终点更新为**两者的较大值**；否则直接加入结果。
- **易错点**：`[1,5]` 和 `[2,4]` 合并后还是 `[1,5]`。终点必须取 max，不能直接用后一个区间的终点。
- 端点相接也算重叠，比如 `[1,4]` 和 `[4,5]` 要合并成 `[1,5]`。

```python
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
```

## 第 36 集 · 435. 无重叠区间

**题意**：最少删除几个区间，才能让剩下的区间互不重叠？

- 排序后依次比较，遇到重叠就必须删掉其中一个。
- **贪心：删掉终点更大的那一个**。留下的区间结束得越早，越不容易和后面的区间重叠。所以重叠时 `prev_end = min(end, prev_end)`，删除数加 1。
- 这道题中端点相接（`[1,2]` 和 `[2,3]`）**不算**重叠，所以判断条件是 `start >= prev_end`。

```python
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
```

## 第 37 集 · 252. 会议室（会员题）

**题意**：给出一组会议时间，判断一个人能否参加所有会议。

- 按开始时间排序后，检查**每两个相邻的会议**：后一个会议的开始时间早于前一个的结束时间，就冲突了。
- 排序 O(n log n)，扫描 O(n)。

```python
# 一个人能否参加所有会议 = 按开始时间排序后，相邻两个会议不重叠
def can_attend_meetings(intervals: List[List[int]]) -> bool:
    intervals = sorted(intervals)
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True
```

## 第 38 集 · 253. 会议室 II（会员题）

**题意**：最少需要几间会议室？

- **本质**：求**同一时刻最多有几个会议同时进行**。
- **视频的解法**：把开始时间和结束时间**分别排序**，用两个指针在时间轴上扫描：
  - 下一个事件是"开始"（`start[s] < end[e]`）：同时进行的会议数加 1，s 后移；
  - 否则是"结束"：会议数减 1，e 后移；
  - 过程中会议数的最大值就是答案。
- **同一时刻一个结束、一个开始**时，先处理结束，因为会议室可以马上复用。所以条件写严格小于 `<`。
- 补充的**最小堆解法**：堆里存"正在进行的会议的结束时间"。新会议开始时，如果最早结束的会议已经结束，就弹出它，复用那间房；最后堆的大小就是答案。

```python
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
```

## 运行结果

运行 `python c05_interval.py` 的实际输出：

```text
57  insert([[1,3],[6,9]], [2,5]) -> [[1, 5], [6, 9]]
57  insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) -> [[1, 2], [3, 10], [12, 16]]
56  merge([[1,3],[2,6],[8,10],[15,18]]) -> [[1, 6], [8, 10], [15, 18]] | [[1,5],[2,4]] -> [[1, 5]]
435 erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]) -> 1 | [[1,2],[1,2],[1,2]] -> 2
252 can_attend_meetings([[0,30],[5,10],[15,20]]) -> False | [[7,10],[2,4]] -> True
253 min_meeting_rooms([[0,30],[5,10],[15,20]]) -> 2 | 堆版 -> 2
253 min_meeting_rooms([[0,40],[5,10],[15,20],[5,25]]) -> 3 | 堆版 -> 3
```

## 本专题要点
- 区间题先**按起点排序**。
- 合并时终点取 **max**；删除时保留**终点更小**的那个（贪心）。
- 搞清楚题目里"端点相接"算不算重叠。
- "需要多少资源"这类问题，本质是求**同时进行的最大数量**：把开始和结束拆开排序扫描，或者用最小堆。


---

# 专题 6：链表 Linked List（第 39～44 集）

> 链表题的三件法宝：
> 1. **哑结点 dummy**：在头结点前面加一个假结点，"删除头结点""结果为空"这类边界情况就不用特殊处理了；
> 2. **快慢指针**：找中点、判断有没有环、找倒数第 n 个结点；
> 3. **反转链表**：很多题的子步骤，必须能闭着眼写出来。
>
> 操作指针前，先把要用的 `next` **存到临时变量里**，否则改了箭头就找不回来了。

| 集 | 题目 | 难度 | 关键技巧 | 时间 / 空间 |
| --- | --- | --- | --- | --- |
| 39 | [206. Reverse Linked List](https://leetcode.cn/problems/reverse-linked-list/) | Easy | 迭代：prev / curr；递归 | O(n) / O(1) 或 O(n) |
| 40 | [141. Linked List Cycle](https://leetcode.cn/problems/linked-list-cycle/) | Easy | Floyd 龟兔赛跑 | O(n) / O(1) |
| 41 | [21. Merge Two Sorted Lists](https://leetcode.cn/problems/merge-two-sorted-lists/) | Easy | 哑结点 + 谁小接谁 | O(m+n) / O(1) |
| 42 | [23. Merge k Sorted Lists](https://leetcode.cn/problems/merge-k-sorted-lists/) | Hard | 两两合并（归并思想）/ 最小堆 | O(N log k) / O(k) |
| 43 | [19. Remove Nth Node From End of List](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/) | Medium | 右指针先走 n 步 + 哑结点 | O(n) / O(1) |
| 44 | [143. Reorder List](https://leetcode.cn/problems/reorder-list/) | Medium | 找中点 → 反转后半段 → 交替合并 | O(n) / O(1) |

---

## 第 39 集 · 206. 反转链表

NeetCode 两种写法都讲了：

- **迭代（推荐）**：两个指针 `prev = None`、`curr = head`。每一步：
  1. 先存下 `nxt = curr.next`；
  2. 反转箭头：`curr.next = prev`；
  3. 两个指针同时前进：`prev = curr`，`curr = nxt`。
  
  结束时 `prev` 就是新的头结点。时间 O(n)，空间 O(1)。
- **递归**：先把 `head.next` 之后的部分反转好，再让 `head.next.next = head`（下一个结点指回自己），最后 `head.next = None`。空间 O(n)，来自递归调用栈。

```python
# 迭代：prev / curr 两个指针，先保存 next，再把箭头反过来   O(n) / O(1)
def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev, curr = curr, nxt
    return prev


# 递归：后面的先反转好，再让下一个结点指回自己   O(n) / O(n)
def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    new_head = head
    if head.next:
        new_head = reverse_list_recursive(head.next)
        head.next.next = head
    head.next = None
    return new_head
```

## 第 40 集 · 141. 环形链表（Floyd 龟兔赛跑）

- **哈希集合解法**：把访问过的结点放进集合，遇到重复的就说明有环，空间 O(n)。
- **快慢指针（Floyd 算法）**：慢指针每次走 1 步，快指针每次走 2 步。
  - 没有环：快指针会先走到 None；
  - 有环：两个指针都进入环之后，**每走一轮，快指针和慢指针的距离缩小 1**，所以一定会相遇，不会"跳过"对方。
  - 相遇前最多走 n 轮，时间 O(n)，空间 O(1)。

```python
# 快指针每次 2 步，慢指针每次 1 步；有环时每走一轮两者距离缩小 1，必定相遇
def has_cycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False
```

## 第 41 集 · 21. 合并两个有序链表

- 建一个**哑结点 dummy**，用 `tail` 指向结果链表的末尾。
- 两个链表都不为空时，**谁小就把谁接到 tail 后面**，然后对应的指针和 tail 前进一步。
- 其中一个走完后，把另一个**剩下的部分整个接上**即可。
- 最后返回 `dummy.next`。

```python
# 哑结点 dummy 避免处理"空链表"的边界情况
def merge_two_lists(l1, l2):
    dummy = tail = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2                     # 剩下的直接接上
    return dummy.next
```

## 第 42 集 · 23. 合并 K 个升序链表（Hard）

- **暴力**：逐个合并，第 1 个和第 2 个合并，结果再和第 3 个合并……总时间 O(N·k)，N 是结点总数。
- **视频的解法：两两合并**，就是归并排序的合并阶段。每一轮把相邻的两个链表合并成一个，**链表数量减半**，一共 log k 轮，每轮处理 N 个结点，总共 **O(N log k)**。直接复用 21 题的函数。
- 补充的**最小堆解法**：堆里放 k 个链表的头结点，每次弹出最小的接到结果上，再把它的下一个结点放进堆。时间同样是 O(N log k)。

```python
# 视频的方法：两两合并（类似归并排序的合并阶段），每轮链表数减半 -> O(N log k)
def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None
    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(merge_two_lists(l1, l2))
        lists = merged
    return lists[0]


# 另一种常见方法：最小堆，每次取 k 个链表头里最小的
def merge_k_lists_heap(lists):
    heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
    heapq.heapify(heap)
    dummy = tail = ListNode()
    while heap:
        _, i, node = heapq.heappop(heap)
        tail.next = tail = node
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next
```

## 第 43 集 · 19. 删除链表的倒数第 N 个结点

- **暴力**：先遍历一遍求长度，再走到倒数第 n+1 个结点，需要两遍。
- **一遍扫描**：
  - 右指针先走 **n 步**，和左指针拉开距离；
  - 两个指针同速前进，右指针走到 None 时，左指针正好在倒数第 n 个结点。
  - 但删除结点需要停在它的**前一个**，所以**左指针从哑结点 dummy 出发**，多退一步。
- 哑结点还能处理"删除的是头结点"的情况，比如 `[1]` 删除倒数第 1 个，结果是空链表。

```python
# 右指针先走 n 步，再和左指针一起走；左指针从 dummy 出发，最后停在"待删结点的前一个"
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    left, right = dummy, head
    for _ in range(n):
        right = right.next
    while right:
        left, right = left.next, right.next
    left.next = left.next.next
    return dummy.next
```

## 第 44 集 · 143. 重排链表

**题意**：把 `L0→L1→…→Ln` 重排成 `L0→Ln→L1→Ln-1→L2→…`，要求原地修改。

- 观察可以发现：结果是**前半段**和**反转后的后半段**交替穿插而成。
- 三步走，每一步都是前面学过的基本功：
  1. **快慢指针找中点**：`fast` 从 `head.next` 出发，结束时 `slow` 停在前半段的末尾。把 `slow.next` 断开，分成两段；
  2. **反转后半段**（206 题）；
  3. **交替合并**：每次先存下两段各自的 `next`，再把后半段的结点插到前半段的结点后面。
- 时间 O(n)，空间 O(1)。

```python
# L0→Ln→L1→Ln-1→...  三步：快慢指针找中点 -> 反转后半段 -> 两段交替合并
def reorder_list(head) -> None:
    slow, fast = head, head.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    second = slow.next                       # 后半段的开头
    slow.next = None                         # 切断
    prev = None
    while second:                            # 反转后半段
        nxt = second.next
        second.next = prev
        prev, second = second, nxt
    first, second = head, prev
    while second:                            # 交替合并
        t1, t2 = first.next, second.next
        first.next = second
        second.next = t1
        first, second = t1, t2
```

## 运行结果

运行 `python c06_linked_list.py` 的实际输出：

```text
206 reverse_list([1,2,3,4,5]) -> [5, 4, 3, 2, 1] | 递归版 -> [5, 4, 3, 2, 1]
141 has_cycle(3,2,0,-4 尾部连回 2) -> True | [1,2] -> False
21  merge_two_lists([1,2,4],[1,3,4]) -> [1, 1, 2, 3, 4, 4]
23  merge_k_lists([1,4,5],[1,3,4],[2,6]) -> [1, 1, 2, 3, 4, 4, 5, 6] | 堆版 -> [1, 1, 2, 3, 4, 4, 5, 6]
19  remove_nth_from_end([1,2,3,4,5], 2) -> [1, 2, 3, 5] | ([1], 1) -> []
143 reorder_list([1, 2, 3, 4]) -> [1, 4, 2, 3]
143 reorder_list([1, 2, 3, 4, 5]) -> [1, 5, 2, 4, 3]
```

## 本专题要点
- 改指针之前，先**保存 next**。
- **哑结点**能省掉大部分头结点相关的边界判断（19、21 题）。
- **快慢指针**：走一步 / 走两步可以判环、找中点；先拉开 n 步可以找倒数第 n 个结点。
- 复杂的链表题往往是**几个基本操作的组合**（143 题 = 找中点 + 反转 + 合并）。
- 合并多个有序序列：两两合并（分治）或最小堆，都是 O(N log k)。


---

# 专题 7：矩阵 Matrix（第 45～48 集）

> 矩阵题考的主要是**下标操作的细心程度**，以及**原地修改**（O(1) 额外空间）。
> NeetCode 的建议是：**先在纸上画出来**，弄清楚每个下标怎么变化，再写代码。

| 集 | 题目 | 难度 | 关键技巧 | 时间 / 空间 |
| --- | --- | --- | --- | --- |
| 45 | [73. Set Matrix Zeroes](https://leetcode.cn/problems/set-matrix-zeroes/) | Medium | 用第 0 行、第 0 列当标记 | O(mn) / O(1) |
| 46 | [54. Spiral Matrix](https://leetcode.cn/problems/spiral-matrix/) | Medium | 四条边界一圈圈收缩 | O(mn) / O(1) |
| 47 | [48. Rotate Image](https://leetcode.cn/problems/rotate-image/) | Medium | 四个角轮换；或者翻转 + 转置 | O(n²) / O(1) |
| 48 | [79. Word Search](https://leetcode.cn/problems/word-search/) | Medium | 回溯 DFS + 路径集合 | O(mn·4^L) / O(L) |

---

## 第 45 集 · 73. 矩阵置零

**题意**：某个元素为 0，就把它所在的整行、整列都置为 0，要求原地修改。

- **不能边扫边改**：刚改出来的 0 会被误认为是原来的 0，导致越改越多。
- 空间逐步优化：
  - O(mn)：复制一份矩阵作为参照；
  - O(m+n)：用两个数组分别记录哪些行、哪些列要清零；
  - **O(1)**：把这两个标记数组**放进矩阵自己的第 0 行和第 0 列**。
- O(1) 解法的细节：
  - `matrix[0][0]` 只能表示一个含义。NeetCode 让它表示"**第 0 列**要清零"，再用一个额外的变量 `row_zero` 表示"**第 0 行**要清零"；
  - **处理顺序很重要**：先处理内部的格子，再处理第 0 列，最后处理第 0 行。否则标记会提前被覆盖。

```python
# O(1) 额外空间：用第 0 行、第 0 列当"标记数组"；第 0 行自己是否要清零，用一个变量单独记
def set_zeroes(matrix: List[List[int]]) -> None:
    rows, cols = len(matrix), len(matrix[0])
    row_zero = False                         # 第 0 行是否需要清零
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0             # 标记这一列
                if r > 0:
                    matrix[r][0] = 0         # 标记这一行
                else:
                    row_zero = True
    for r in range(1, rows):                 # 先处理除第 0 行、第 0 列以外的格子
        for c in range(1, cols):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
    if matrix[0][0] == 0:                    # 第 0 列
        for r in range(rows):
            matrix[r][0] = 0
    if row_zero:                             # 第 0 行
        for c in range(cols):
            matrix[0][c] = 0
```

## 第 46 集 · 54. 螺旋矩阵

**题意**：按顺时针螺旋顺序返回矩阵的所有元素。

- 维护四条边界 `left`、`right`、`top`、`bottom`（right 和 bottom 是开区间）。
- 每一圈依次走四条边，每走完一条就收缩对应的边界：
  1. 上边从左到右，然后 `top += 1`；
  2. 右边从上到下，然后 `right -= 1`；
  3. 下边从右到左，然后 `bottom -= 1`；
  4. 左边从下到上，然后 `left += 1`。
- **易错点**：矩阵不是正方形时，最后可能只剩**一行或一列**。走完上边和右边后要再检查一次边界，否则会把同一批元素重复加入。

```python
# 四条边界 left/right/top/bottom，按"上 -> 右 -> 下 -> 左"一圈圈收缩
def spiral_order(matrix: List[List[int]]) -> List[int]:
    res = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    while left < right and top < bottom:
        for i in range(left, right):         # 上边，从左到右
            res.append(matrix[top][i])
        top += 1
        for i in range(top, bottom):         # 右边，从上到下
            res.append(matrix[i][right - 1])
        right -= 1
        if not (left < right and top < bottom):
            break                            # 只剩一行或一列时，避免重复
        for i in range(right - 1, left - 1, -1):   # 下边，从右到左
            res.append(matrix[bottom - 1][i])
        bottom -= 1
        for i in range(bottom - 1, top - 1, -1):   # 左边，从下到上
            res.append(matrix[i][left])
        left += 1
    return res
```

## 第 47 集 · 48. 旋转图像

**题意**：把 n×n 矩阵顺时针旋转 90 度，必须原地修改。

- **视频的方法：一圈圈地旋转**。最外圈处理完再处理内圈（`l += 1`，`r -= 1`）。
  - 每一圈中，**四个位置为一组**，按顺时针轮换：左下 → 左上，右下 → 左下，右上 → 右下，左上 → 右上；
  - NeetCode 的技巧是**逆时针方向赋值**，这样只需要一个临时变量保存左上角的值；
  - 每圈有 `r - l` 组，用偏移量 `i` 表示。
- **补充的好记方法**：先**上下翻转**，再沿**主对角线转置**，效果等于顺时针旋转 90 度。

```python
# 一圈圈处理：每次把四个角上对应的元素顺时针轮换（只用一个临时变量）
def rotate(matrix: List[List[int]]) -> None:
    l, r = 0, len(matrix) - 1
    while l < r:
        for i in range(r - l):
            top, bottom = l, r
            top_left = matrix[top][l + i]                      # 保存左上
            matrix[top][l + i] = matrix[bottom - i][l]         # 左下 -> 左上
            matrix[bottom - i][l] = matrix[bottom][r - i]      # 右下 -> 左下
            matrix[bottom][r - i] = matrix[top + i][r]         # 右上 -> 右下
            matrix[top + i][r] = top_left                      # 左上 -> 右上
        l += 1
        r -= 1


# 另一种好记的方法：先上下翻转，再沿主对角线转置
def rotate_flip(matrix: List[List[int]]) -> None:
    matrix.reverse()
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

## 第 48 集 · 79. 单词搜索（回溯）

**题意**：网格中能否沿上下左右相邻的格子拼出 word？同一个格子不能重复使用。

- 从**每个格子**出发做 DFS，参数是 `(r, c, i)`，表示当前要匹配 `word[i]`。
- 返回 False 的情况：越界、字符不匹配、格子已经在**当前路径**上。
- `i == len(word)` 说明整个单词都匹配上了，返回 True。
- **回溯**：DFS 返回前把当前格子从 `path` 中移除，让其他路径还能用它。
- 时间复杂度：起点有 m·n 个，每一步最多 4 个方向，深度为单词长度 L，所以是 O(m·n·4^L)。

```python
# 从每个格子出发 DFS；path 记录当前路径上的格子（同一个格子不能用两次），回溯时移除
def exist(board: List[List[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])
    path = set()

    def dfs(r, c, i):
        if i == len(word):
            return True
        if (r < 0 or c < 0 or r >= rows or c >= cols
                or word[i] != board[r][c] or (r, c) in path):
            return False
        path.add((r, c))
        res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1)
               or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
        path.remove((r, c))                  # 回溯
        return res

    return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))
```

## 运行结果

运行 `python c07_matrix.py` 的实际输出：

```text
73 set_zeroes([[1,1,1],[1,0,1],[1,1,1]]) -> [1, 0, 1] [0, 0, 0] [1, 0, 1]
73 set_zeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]) -> [0, 0, 0, 0] [0, 4, 5, 0] [0, 3, 1, 0]
54 spiral_order(3x3) -> [1, 2, 3, 6, 9, 8, 7, 4, 5]
54 spiral_order(3x4) -> [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
48 rotate(3x3) -> [7, 4, 1] [8, 5, 2] [9, 6, 3] | 翻转+转置版 -> [7, 4, 1] [8, 5, 2] [9, 6, 3]
48 rotate(4x4) -> [15, 13, 2, 5] [14, 3, 4, 1] [12, 6, 8, 9] [16, 7, 10, 11]
79 exist(board, 'ABCCED') -> True | 'SEE' -> True | 'ABCB' -> False
```

## 本专题要点
- 原地修改时，警惕"刚改的值被当成原始值"，可以借用矩阵自身的一部分来存标记。
- 螺旋、旋转这类题：用**边界变量**控制范围，一圈圈处理，并注意只剩一行或一列的情况。
- 网格回溯：进入时加入路径，返回前移除；越界、不匹配、重复访问都要剪掉。


---

# 专题 8：字符串 String（第 49～57 集 + 第 74 集）

> 字符串题的三大工具：
> - **滑动窗口**：求"最长 / 最短的连续子串"，用左右指针维护一个合法的窗口（3、424、76 题）；
> - **哈希计数**：判断字母异位词、统计字符频次（49、242 题）；
> - **双指针 / 中心扩展**：处理回文（125、5、647 题）。
>
> 第 74 集 Valid Anagram 在播放列表的后面，因为属于字符串题，放在本专题里一起讲。

| 集 | 题目 | 难度 | 关键技巧 | 时间 / 空间 |
| --- | --- | --- | --- | --- |
| 49 | [3. Longest Substring Without Repeating Characters](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) | Medium | 滑动窗口 + 集合 | O(n) / O(字符集) |
| 50 | [424. Longest Repeating Character Replacement](https://leetcode.cn/problems/longest-repeating-character-replacement/) | Medium | 窗口长度 − 最多字符数 ≤ k | O(n) / O(26) |
| 51 | [76. Minimum Window Substring](https://leetcode.cn/problems/minimum-window-substring/) | Hard | 两个计数表 + have/need | O(n) / O(字符集) |
| 52 | [49. Group Anagrams](https://leetcode.cn/problems/group-anagrams/) | Medium | 26 位计数作为 key | O(m·n) / O(m·n) |
| 53 | [20. Valid Parentheses](https://leetcode.cn/problems/valid-parentheses/) | Easy | 栈 | O(n) / O(n) |
| 54 | [125. Valid Palindrome](https://leetcode.cn/problems/valid-palindrome/) | Easy | 双指针，跳过非字母数字 | O(n) / O(1) |
| 55 | [5. Longest Palindromic Substring](https://leetcode.cn/problems/longest-palindromic-substring/) | Medium | 中心扩展（奇数 + 偶数） | O(n²) / O(1) |
| 56 | [647. Palindromic Substrings](https://leetcode.cn/problems/palindromic-substrings/) | Medium | 中心扩展计数 | O(n²) / O(1) |
| 57 | [271. Encode and Decode Strings](https://leetcode.cn/problems/encode-and-decode-strings/)（会员） | Medium | 长度 + 分隔符 `#` | O(n) / O(n) |
| 74 | [242. Valid Anagram](https://leetcode.cn/problems/valid-anagram/) | Easy | 两个哈希表计数 | O(n) / O(26) |

---

## 第 49 集 · 3. 无重复字符的最长子串

- **滑动窗口**：右指针 r 每次加入一个新字符。如果这个字符**已经在窗口里**，就从左边一直删字符、左指针右移，直到窗口里没有重复为止。
- 用**集合**记录窗口里的字符，查找是 O(1)。
- 每个字符最多进出窗口各一次，时间 O(n)。

```python
# 滑动窗口 + 集合：右边加入的字符重复了，就从左边一直删到不重复为止
def length_of_longest_substring(s: str) -> int:
    char_set = set()
    l = res = 0
    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        res = max(res, r - l + 1)
    return res
```

## 第 50 集 · 424. 替换后的最长重复字符

**题意**：最多可以把 k 个字符替换成任意字符，求替换后由相同字母组成的最长子串长度。

- **关键观察**：把窗口里的字符都变成**出现次数最多的那个字符**，需要替换的次数最少，为 `窗口长度 − 最大频次`。只要这个值 ≤ k，窗口就是合法的。
- 窗口不合法时，左指针右移，同时减少对应字符的计数。
- **进阶技巧**：`maxf`（历史最大频次）**只增不减**，不需要在收缩窗口时重新计算。原因是只有 maxf 变大时，答案才可能变大；maxf 偏大只会让窗口暂时保持原来的长度，不会得出错误的更大答案。这样每一步都是 O(1)，不用每次扫描 26 个字母。

```python
# 窗口合法 <=> 窗口长度 - 窗口内出现最多的字符次数 <= k（需要替换的字符数）
def character_replacement(s: str, k: int) -> int:
    count = {}
    res = l = 0
    maxf = 0                                 # 技巧：maxf 只增不减，不影响答案
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])
        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res
```

## 第 51 集 · 76. 最小覆盖子串（Hard）

**题意**：在 s 中找出包含 t 的所有字符（包括重复字符）的最短子串。

- 两个计数表：`count_t` 是 t 中每个字符需要的数量，`window` 是当前窗口中每个字符的数量。
- **have / need 技巧**：`need` 是 t 中不同字符的种类数；`have` 是窗口中**数量已经满足要求**的字符种类数。这样判断"窗口是否覆盖了 t"只需比较两个整数，是 O(1)，不用每次比较整张表。
- 流程：
  1. 右指针扩张，某个字符的数量**刚好达到**要求时，`have += 1`；
  2. 当 `have == need` 时，记录当前窗口长度，然后**尽量收缩左边**；某个字符的数量少于要求时，`have -= 1`，停止收缩。
- 时间 O(n)。

```python
# 两个计数表 + have/need：右指针扩张直到满足条件，然后左指针收缩求最小
def min_window(s: str, t: str) -> str:
    if t == "":
        return ""
    count_t, window = {}, {}
    for c in t:
        count_t[c] = 1 + count_t.get(c, 0)
    have, need = 0, len(count_t)             # 满足要求的"字符种类数"
    res, res_len = [-1, -1], float("inf")
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)
        if c in count_t and window[c] == count_t[c]:
            have += 1
        while have == need:
            if (r - l + 1) < res_len:
                res, res_len = [l, r], r - l + 1
            window[s[l]] -= 1                # 收缩左边
            if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l:r + 1] if res_len != float("inf") else ""
```

## 第 52 集 · 49. 字母异位词分组

- **排序作为 key**：异位词排序后完全相同，但每个单词排序要 O(n log n)。
- **NeetCode 的方法：用字符计数作为 key**。题目说只有小写字母，所以用长度为 26 的计数数组，每个单词 O(n) 就能算出来。
- Python 的 list 不能作为字典的 key，要转成 **tuple**。
- 总时间 O(m·n)，m 是单词个数，n 是平均长度。

```python
# key = 26 个字母的计数（元组），O(m * n)，比排序 O(m * n log n) 更快
def group_anagrams(strs: List[str]) -> List[List[str]]:
    ans = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)          # list 不能当 key，要转成 tuple
    return list(ans.values())
```

## 第 53 集 · 20. 有效的括号

- **栈**：左括号入栈；遇到右括号时，**栈顶必须是对应的左括号**，是就出栈，不是就无效。
- 用哈希表 `右括号 → 左括号` 简化判断。
- 最后栈必须为空，比如 `"(("` 就无效。

```python
# 栈：遇到右括号时，栈顶必须是对应的左括号
def is_valid(s: str) -> bool:
    stack = []
    close_to_open = {")": "(", "]": "[", "}": "{"}
    for c in s:
        if c in close_to_open:
            if stack and stack[-1] == close_to_open[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return not stack
```

## 第 54 集 · 125. 验证回文串

**题意**：只考虑字母和数字，忽略大小写，判断是否是回文。

- **简单写法**：过滤出字母和数字、转成小写，再和反转后的字符串比较。但这需要 O(n) 额外空间。
- **双指针**：左右指针向中间走，**跳过非字母数字字符**，比较时忽略大小写，额外空间 O(1)。
- NeetCode 在视频里自己实现了判断字母数字的函数（比较 ASCII 码），因为面试官可能不允许用 `isalnum()`。

```python
# 双指针，跳过非字母数字字符，忽略大小写；不额外建新字符串 -> O(1) 空间
def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True
```

## 第 55 集 · 5. 最长回文子串

- **暴力**：枚举所有子串再判断是否回文，O(n³)。
- **中心扩展**：回文从中心向两边对称。以**每个字符**为中心（奇数长度），以及以**每两个相邻字符之间**为中心（偶数长度），向两边扩展，直到左右字符不相等。
- 一共 2n-1 个中心，每次扩展最多 O(n)，总时间 O(n²)，空间 O(1)。

```python
# 中心扩展：每个字符（奇数长度）和每两个字符之间（偶数长度）都当一次中心   O(n^2) / O(1)
def longest_palindrome(s: str) -> str:
    res = ""
    for i in range(len(s)):
        for l, r in ((i, i), (i, i + 1)):    # 奇数中心、偶数中心
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r + 1]
                l, r = l - 1, r + 1
    return res
```

## 第 56 集 · 647. 回文子串

**题意**：统计字符串中回文子串的**个数**。

- 和第 5 题完全相同的中心扩展，只是**每扩展成功一次，计数加 1**，因为每次扩展都对应一个新的回文子串。
- `"aaa"` 的回文子串有 a、a、a、aa、aa、aaa，共 6 个。

```python
# 和第 5 题同一个中心扩展，只是每扩展成功一次就计数 +1
def count_substrings(s: str) -> int:
    res = 0
    for i in range(len(s)):
        for l, r in ((i, i), (i, i + 1)):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l, r = l - 1, r + 1
    return res
```

## 第 57 集 · 271. 字符串的编码与解码（会员题）

**题意**：设计算法，把字符串列表编码成一个字符串，并能解码回原来的列表。字符串里可能包含任何字符。

- **只用分隔符不行**：如果字符串里本身就有分隔符，就无法区分。
- **NeetCode 的方法**：每个字符串编码成 `长度 + "#" + 字符串本身`。
  - 解码时先往后读到 `#`，得到长度，再**直接截取这么多个字符**；
  - 即使字符串里有 `#` 或者数字也没关系，因为截取时根本不看内容；
  - 空字符串编码成 `0#`，也能正确处理。

```python
# 每个字符串前面加 "长度#"。即使字符串里本身含有 '#' 也不会出错，因为先读长度
def encode(strs: List[str]) -> str:
    return "".join(f"{len(s)}#{s}" for s in strs)


def decode(s: str) -> List[str]:
    res, i = [], 0
    while i < len(s):
        j = i
        while s[j] != "#":                   # 读出长度
            j += 1
        length = int(s[i:j])
        res.append(s[j + 1:j + 1 + length])
        i = j + 1 + length
    return res
```

## 第 74 集 · 242. 有效的字母异位词

- 长度不同直接返回 False。
- 用**两个哈希表**分别统计两个字符串的字符频次，然后比较是否相等。时间 O(n)，空间 O(26)。
- **排序法**：`sorted(s) == sorted(t)`，时间 O(n log n)。NeetCode 提到，如果面试官要求 O(1) 空间，可以用排序（假设排序本身不占额外空间）。

```python
# 两个哈希表计数比较；也可以 sorted(s) == sorted(t)（空间更省，时间 O(n log n)）
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count_s, count_t = {}, {}
    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
    return count_s == count_t
```

## 运行结果

运行 `python c08_string.py` 的实际输出：

```text
3   length_of_longest_substring('abcabcbb') -> 3 | 'pwwkew' -> 3
424 character_replacement('ABAB', 2) -> 4 | ('AABABBA', 1) -> 4
76  min_window('ADOBECODEBANC', 'ABC') -> 'BANC' | ('a', 'aa') -> ''
49  group_anagrams(['eat','tea','tan','ate','nat','bat']) -> [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
20  is_valid('()[]{}') -> True | '([)]' -> False | '{[]}' -> True
125 is_palindrome('A man, a plan, a canal: Panama') -> True | 'race a car' -> False
5   longest_palindrome('babad') -> 'bab' | 'cbbd' -> 'bb'
647 count_substrings('abc') -> 3 | 'aaa' -> 6
271 encode(['neet','co#de','','4#x']) -> '4#neet5#co#de0#3#4#x' | decode 回来 -> ['neet', 'co#de', '', '4#x']
242 is_anagram('anagram', 'nagaram') -> True | ('rat', 'car') -> False
```

## 本专题要点
- **滑动窗口模板**：右指针扩张，窗口不合法时左指针收缩，并在合适的时机更新答案。
- 窗口合法性要能 O(1) 判断：424 题用"长度 − 最大频次"，76 题用 have/need。
- 字母异位词 = **字符频次相同**：用计数数组或计数表作为 key 或者进行比较。
- 回文：判断用双指针，查找用**中心扩展**，奇数和偶数两种中心都要考虑。
- 编码含任意字符的数据时，用"**长度前缀**"代替分隔符。


---

# 专题 9：树 Tree（第 58～71 集）

> 树题的核心是**递归**：把问题拆成"左子树的答案 + 右子树的答案 + 当前结点要做的事"。
> - **DFS** 分前序、中序、后序。中序遍历 **BST（二叉搜索树）** 得到的是有序序列，这是很多 BST 题的突破口；
> - **BFS** 用队列一层一层处理，适合和"层"有关的题；
> - **Trie（前缀树）** 是专门处理字符串前缀的树，第 69～71 集。

| 集 | 题目 | 难度 | 关键技巧 | 时间 / 空间 |
| --- | --- | --- | --- | --- |
| 58 | [104. Maximum Depth of Binary Tree](https://leetcode.cn/problems/maximum-depth-of-binary-tree/) | Easy | 递归 DFS / BFS / 迭代 DFS 三种解法 | O(n) / O(h) |
| 59 | [100. Same Tree](https://leetcode.cn/problems/same-tree/) | Easy | 同时递归两棵树 | O(n) / O(h) |
| 60 | [226. Invert Binary Tree](https://leetcode.cn/problems/invert-binary-tree/) | Easy | 交换左右孩子再递归 | O(n) / O(h) |
| 61 | [124. Binary Tree Maximum Path Sum](https://leetcode.cn/problems/binary-tree-maximum-path-sum/) | Hard | 返回"不分叉"的路径，在当前结点"分叉" | O(n) / O(h) |
| 62 | [102. Binary Tree Level Order Traversal](https://leetcode.cn/problems/binary-tree-level-order-traversal/) | Medium | BFS，每次处理一整层 | O(n) / O(n) |
| 63 | [297. Serialize and Deserialize Binary Tree](https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/) | Hard | 前序遍历 + 空结点标记 `N` | O(n) / O(n) |
| 64 | [572. Subtree of Another Tree](https://leetcode.cn/problems/subtree-of-another-tree/) | Easy | 每个结点都调用一次"相同的树" | O(m·n) / O(h) |
| 65 | [105. Construct Binary Tree from Preorder and Inorder](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Medium | 前序首个是根，中序里的位置划分左右 | O(n²)，可优化到 O(n) |
| 66 | [98. Validate Binary Search Tree](https://leetcode.cn/problems/validate-binary-search-tree/) | Medium | 把取值范围 (left, right) 往下传 | O(n) / O(h) |
| 67 | [230. Kth Smallest Element in a BST](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/) | Medium | 迭代中序遍历，数到第 k 个 | O(h+k) / O(h) |
| 68 | [235. Lowest Common Ancestor of a BST](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Medium | 利用 BST 大小关系，看在哪里"分叉" | O(h) / O(1) |
| 69 | [208. Implement Trie](https://leetcode.cn/problems/implement-trie-prefix-tree/) | Medium | 每个结点：children 表 + 单词结尾标记 | O(L) / O(总字符数) |
| 70 | [211. Design Add and Search Words](https://leetcode.cn/problems/design-add-and-search-words-data-structure/) | Medium | Trie + 遇到 `.` 就 DFS 所有孩子 | O(L)～O(26^L) |
| 71 | [212. Word Search II](https://leetcode.cn/problems/word-search-ii/) | Hard | 所有单词建 Trie + 网格回溯 | O(m·n·4^L) |

h 表示树的高度：平衡树为 log n，最坏（退化成链表）为 n。

---

## 第 58 集 · 104. 二叉树的最大深度（三种解法）

NeetCode 在这一集里把树的**三种遍历方式**都演示了一遍：
1. **递归 DFS**（最简洁）：`1 + max(左子树深度, 右子树深度)`，空结点的深度为 0；
2. **BFS**：用队列一层一层处理，**数一共有几层**；
3. **迭代 DFS**：用栈模拟前序遍历，栈里存 `(结点, 当前深度)`，过程中记录最大深度。

三种方法都是 O(n)。面试时能说出三种写法，说明你对树的遍历非常熟悉。

```python
# 1) 递归 DFS
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# 2) BFS：数一共有几层
def max_depth_bfs(root):
    if not root:
        return 0
    level, q = 0, deque([root])
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level


# 3) 迭代 DFS：栈里存 (结点, 深度)，模拟前序遍历
def max_depth_iter(root):
    stack, res = [(root, 1)], 0
    while stack:
        node, depth = stack.pop()
        if node:
            res = max(res, depth)
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))
    return res
```

## 第 59 集 · 100. 相同的树

- **同时递归两棵树**：
  - 两个结点都为空：相同；
  - 只有一个为空，或者值不同：不同；
  - 否则递归比较左子树和左子树、右子树和右子树。
- 这个函数会在第 64 集中被复用。

```python
def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
```

## 第 60 集 · 226. 翻转二叉树

- 对每个结点，**交换它的左右孩子**，再递归翻转左右子树。用前序或后序都可以。
- 这道题因为一则"Homebrew 的作者面试谷歌没写出这道题"的趣闻而出名，其实只有几行代码。

```python
def invert_tree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root
```

## 第 61 集 · 124. 二叉树中的最大路径和（Hard）

- 路径可以在某个结点**"分叉"**：从左子树上来，经过这个结点，再到右子树。但分叉只能发生**一次**。
- **关键**：
  - 递归函数**返回给父结点**的，只能是**不分叉**的路径和，即 `node.val + max(左边, 右边)`。如果在当前结点分叉了，父结点再接上来就不是一条合法的路径了；
  - **在当前结点分叉**的路径和 `node.val + 左边 + 右边`，用来更新**全局答案**；
  - 子树返回的值如果是**负数，就当作 0**，即不选这一边。
- 全局答案的初值设为 `root.val`，不能设为 0，因为树里可能全是负数。

```python
# dfs 返回"不分叉"的最大路径和（只能选一边往下）；在当前结点拼"分叉"路径更新全局答案
def max_path_sum(root):
    res = [root.val]

    def dfs(node):
        if not node:
            return 0
        left_max = max(dfs(node.left), 0)            # 负数不要
        right_max = max(dfs(node.right), 0)
        res[0] = max(res[0], node.val + left_max + right_max)   # 在这里"分叉"
        return node.val + max(left_max, right_max)               # 返回给父结点：不能分叉

    dfs(root)
    return res[0]
```

## 第 62 集 · 102. 二叉树的层序遍历

- **BFS**：队列里放根结点，每一轮先记下**当前队列长度**，正好是这一层的结点数；把它们依次取出、记录值，并把孩子加入队列。
- NeetCode 的写法是把空结点也放进队列，取出时再跳过，这样代码更短。

```python
def level_order(root):
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    return res
```

## 第 63 集 · 297. 二叉树的序列化与反序列化（Hard）

- **序列化**：**前序遍历**，空结点写成 `"N"`，用逗号连接。有了空结点标记，前序序列就能**唯一确定**一棵树。
- **反序列化**：用**同样的前序顺序**依次读取。读到 `"N"` 返回空结点；否则新建结点，再递归构造左子树和右子树。用一个全局下标 i 记录读到了哪里。
- 时间和空间都是 O(n)。

```python
# 前序遍历，空结点写 "N"；反序列化时用同样的前序顺序依次读取
def serialize(root) -> str:
    res = []

    def dfs(node):
        if not node:
            res.append("N")
            return
        res.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ",".join(res)


def deserialize(data: str):
    vals = data.split(",")
    i = 0

    def dfs():
        nonlocal i
        if vals[i] == "N":
            i += 1
            return None
        node = TreeNode(int(vals[i]))
        i += 1
        node.left = dfs()
        node.right = dfs()
        return node

    return dfs()
```

## 第 64 集 · 572. 另一棵树的子树

- 对 root 的**每一个结点**，都检查以它为根的子树和 sub_root 是否**完全相同**（复用 100 题）。
- 边界情况：sub_root 为空，一定是子树；root 为空而 sub_root 不为空，一定不是。
- 时间 O(m·n)。
- 注意第二个例子：`[4,1,2]` 的结构虽然出现在了 root 中，但那个 2 下面还多挂了一个 0，所以**不完全相同**，返回 False。

```python
# 对 root 的每个结点，都检查"以它为根的子树"和 sub_root 是否相同（复用 100 题）
def is_subtree(root, sub_root):
    if not sub_root:
        return True
    if not root:
        return False
    if is_same_tree(root, sub_root):
        return True
    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)
```

## 第 65 集 · 105. 从前序与中序遍历序列构造二叉树

- **前序的第一个元素一定是根**。
- 在**中序**里找到根的位置 mid：**mid 左边的是左子树，右边的是右子树**，左子树一共有 mid 个结点。
- 所以前序里，根后面的 mid 个元素 `preorder[1 : mid+1]` 是左子树，再往后 `preorder[mid+1 :]` 是右子树。递归构造即可。
- 优化：用哈希表预先存好"值 → 中序下标"，用下标代替切片，可以把时间从 O(n²) 降到 O(n)。

```python
# 前序第一个 = 根；在中序里找到根的位置 mid：左边 mid 个是左子树，右边是右子树
def build_tree_from(preorder: List[int], inorder: List[int]):
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = build_tree_from(preorder[1:mid + 1], inorder[:mid])
    root.right = build_tree_from(preorder[mid + 1:], inorder[mid + 1:])
    return root
```

## 第 66 集 · 98. 验证二叉搜索树

- **常见错误**：只检查"左孩子 < 父结点 < 右孩子"。`[5,4,6,null,null,3,7]` 中，3 是 6 的左孩子，满足父子关系，但它在 5 的**右子树**里，却比 5 小，所以不是 BST。
- **正确做法**：把每个结点**允许的取值范围** `(left, right)` 往下传：
  - 往左走：上界变成当前结点的值；
  - 往右走：下界变成当前结点的值；
  - 根结点的范围是 `(-∞, +∞)`。
- 另一种思路：BST 的中序遍历必须**严格递增**。

```python
# 只比较父子不够！要把每个结点允许的取值范围 (left, right) 往下传
def is_valid_bst(root):
    def valid(node, left, right):
        if not node:
            return True
        if not (left < node.val < right):
            return False
        return valid(node.left, left, node.val) and valid(node.right, node.val, right)

    return valid(root, float("-inf"), float("inf"))
```

## 第 67 集 · 230. 二叉搜索树中第 K 小的元素

- **BST 的中序遍历是有序的**，所以中序遍历时数到第 k 个就是答案。
- NeetCode 用**迭代**中序遍历：
  1. 一直往左走，把沿途的结点压入栈；
  2. 弹出栈顶并计数，数到 k 就返回；
  3. 然后转到它的右子树，重复第 1 步。
- 迭代写法可以**数到第 k 个就停下**，不用遍历整棵树。

```python
# BST 的中序遍历是有序的：迭代中序遍历，数到第 k 个就停
def kth_smallest(root, k: int) -> int:
    n, stack, cur = 0, [], root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        n += 1
        if n == k:
            return cur.val
        cur = cur.right
```

## 第 68 集 · 235. 二叉搜索树的最近公共祖先

- 利用 BST 的大小关系，从根往下走：
  - p 和 q **都比当前结点大**：LCA 在右子树；
  - **都比当前结点小**：LCA 在左子树；
  - 否则，p 和 q 在当前结点**分叉**（一个在左、一个在右），或者其中一个就是当前结点，**当前结点就是 LCA**。
- 只走一条从根往下的路径，时间 O(h)，空间 O(1)。

```python
# 都比当前大 -> 往右；都比当前小 -> 往左；否则（分叉或等于当前）当前就是答案
def lowest_common_ancestor(root, p, q):
    cur = root
    while cur:
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
        else:
            return cur
```

## 第 69 集 · 208. 实现 Trie（前缀树）

- 每个结点有两个属性：`children`（字符 → 子结点的哈希表）和 `end_of_word`（是不是某个单词的结尾）。
- **insert**：沿着字符往下走，没有对应的子结点就新建，最后把结尾结点标记为 `end_of_word = True`。
- **search**：沿着字符往下走，中途走不通返回 False；走完后还必须是**单词结尾**。比如只插入了 `"apple"`，`search("app")` 返回 False。
- **startsWith**：只要能走完前缀就返回 True。
- 优点：查找一个长度为 L 的单词或前缀只需 O(L)，**和存了多少单词无关**。

```python
class TrieNode:
    def __init__(self):
        self.children = {}                   # 字符 -> TrieNode
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end_of_word               # 必须是一个完整单词的结尾

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True                          # 前缀存在即可
```

## 第 70 集 · 211. 添加与搜索单词

- 在 Trie 的基础上，搜索时支持 `.` 通配符，它可以匹配任意一个字母。
- 遇到 `.` 时，不知道该走哪个孩子，就**对当前结点的所有孩子都做一次 DFS**，从下一个字符继续匹配，有一条路成功就返回 True。
- 没有 `.` 时是 O(L)；最坏情况全是 `.`，需要遍历整棵 Trie。

```python
# 遇到 '.' 时，对当前结点的所有孩子做 DFS
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.children.setdefault(c, TrieNode())
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    return any(dfs(i + 1, child) for child in cur.children.values())
                if c not in cur.children:
                    return False
                cur = cur.children[c]
            return cur.end_of_word

        return dfs(0, self.root)
```

## 第 71 集 · 212. 单词搜索 II（Hard）

**题意**：在字母网格中，找出单词列表里所有能被拼出来的单词。

- **暴力**：对每个单词都做一次 79 题（单词搜索），单词很多时会超时。
- **Trie + 回溯**：
  1. 先把**所有单词**插入一棵 Trie；
  2. 从每个格子出发 DFS，**同时沿着 Trie 往下走**。当前路径组成的前缀在 Trie 里不存在，就**立刻剪枝**；
  3. 走到 `end_of_word` 的结点，就把当前单词加入结果。用集合去重，因为同一个单词可能有多条路径；
  4. 回溯：返回前把格子从 `visit` 中移除。
- 一次 DFS 能同时匹配所有拥有共同前缀的单词，这就是 Trie 的威力。

```python
# 把所有单词放进 Trie，从每个格子出发 DFS，沿着 Trie 往下走：前缀不存在立刻剪枝
def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    root = TrieNode()
    for w in words:
        cur = root
        for c in w:
            cur = cur.children.setdefault(c, TrieNode())
        cur.end_of_word = True
    rows, cols = len(board), len(board[0])
    res, visit = set(), set()

    def dfs(r, c, node, word):
        if (r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit
                or board[r][c] not in node.children):
            return
        visit.add((r, c))
        node = node.children[board[r][c]]
        word += board[r][c]
        if node.end_of_word:
            res.add(word)
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc, node, word)
        visit.remove((r, c))                 # 回溯

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root, "")
    return sorted(res)
```

## 运行结果

运行 `python c09_tree.py` 的实际输出：

```text
104 max_depth([3,9,20,null,null,15,7]) -> 递归 3 | BFS 3 | 迭代DFS 3
100 is_same_tree([1,2,3],[1,2,3]) -> True | ([1,2],[1,null,2]) -> False
226 invert_tree([4,2,7,1,3,6,9]) -> [4, 7, 2, 9, 6, 3, 1]
124 max_path_sum([-10,9,20,null,null,15,7]) -> 42 | [-3] -> -3
102 level_order([3,9,20,null,null,15,7]) -> [[3], [9, 20], [15, 7]]
297 serialize([1,2,3,null,null,4,5]) -> '1,2,N,N,3,4,N,N,5,N,N' | deserialize 回来 -> [1, 2, 3, None, None, 4, 5]
572 is_subtree([3,4,5,1,2],[4,1,2]) -> True | ([3,4,5,1,2,null,null,null,null,0],[4,1,2]) -> False
105 build_tree_from([3,9,20,15,7],[9,3,15,20,7]) -> [3, 9, 20, None, None, 15, 7]
98  is_valid_bst([2,1,3]) -> True | [5,1,4,null,null,3,6] -> False | [5,4,6,null,null,3,7]（3 在 5 的右子树里）-> False
230 kth_smallest([5,3,6,2,4,null,null,1], 3) -> 3
235 LCA(2, 8) -> 6 | LCA(2, 4) -> 2
208 Trie: insert apple -> search('apple') True | search('app') False | startsWith('app') True
211 search('pad'), ('bad'), ('.ad'), ('b..') -> False True True True
212 find_words(board, ['oath','pea','eat','rain']) -> ['eat', 'oath']
```

## 本专题要点
- 绝大多数树题都是**递归**：想清楚"递归函数返回什么"，以及"当前结点要做什么"。
- 题目要的答案和返回给父结点的值**不一样**时（比如 124 题），用全局变量记录答案。
- **BST**：中序遍历有序；验证时要传**取值范围**；找 LCA 时看在哪里**分叉**。
- 序列化：前序遍历 + 空结点标记，就能唯一还原一棵树。
- 和**前缀**有关的字符串问题想到 **Trie**；Trie 和回溯结合可以一次搜索多个单词。


---

# 专题 10：堆 Heap / 优先队列（第 72～73 集）

> Python 的 `heapq` 只有**最小堆**，需要最大堆时**存相反数**。
> 堆适合两类问题：**Top K**（但 347 题有更快的桶排序解法），以及**数据流中的动态最值或中位数**。

| 集 | 题目 | 难度 | 关键技巧 | 时间 / 空间 |
| --- | --- | --- | --- | --- |
| 72 | [347. Top K Frequent Elements](https://leetcode.cn/problems/top-k-frequent-elements/) | Medium | 桶排序：下标 = 出现次数 | O(n) / O(n) |
| 73 | [295. Find Median from Data Stream](https://leetcode.cn/problems/find-median-from-data-stream/) | Hard | 两个堆：最大堆放小的一半，最小堆放大的一半 | 加入 O(log n)，查询 O(1) |

---

## 第 72 集 · 347. 前 K 个高频元素（桶排序）

- 先用哈希表统计每个数的出现次数。
- **常规做法**：
  - 按次数排序，O(n log n)；
  - 用**最小堆**维护前 k 个，O(n log k)。代码中的 `top_k_frequent_heap` 用 `heapq.nlargest` 实现了这个思路。
- **NeetCode 的 O(n) 解法：桶排序**。
  - 关键观察：一个数**最多出现 n 次**，所以次数的范围是 1～n，有上限；
  - 开一个长度为 n+1 的数组 `freq`，**下标是出现次数，值是出现这么多次的数的列表**；
  - 从最大的下标往前收集，凑够 k 个就返回。
- 时间 O(n)，空间 O(n)。

```python
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
```

## 第 73 集 · 295. 数据流的中位数（Hard）

**题意**：不断加入数字，并且随时查询当前所有数的中位数。

- **暴力**：每次查询前排序，或者维护一个有序数组插入新数（插入需要 O(n)）。
- **两个堆**：
  - `small`：**最大堆**，存较小的一半；
  - `large`：**最小堆**，存较大的一半。
  - 中位数只和两个堆的**堆顶**有关，所以查询是 O(1)。
- **需要维持两个条件**：
  1. **顺序**：small 里的每个数都 ≤ large 里的每个数。新数默认先放进 small，如果 small 的堆顶大于 large 的堆顶，就把它挪到 large；
  2. **平衡**：两个堆的大小**最多相差 1**，多了就从多的那边挪一个到另一边。
- **查询**：哪个堆多一个，中位数就是那个堆的堆顶；一样多时，取两个堆顶的平均值。
- 加入 O(log n)，查询 O(1)。

```python
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
```

## 运行结果

运行 `python c10_heap.py` 的实际输出：

```text
347 top_k_frequent([1,1,1,2,2,3], 2) -> [1, 2] | 堆版 -> [1, 2] | ([1], 1) -> [1]
295 依次加入 1,2,3,6,5，每次的中位数 -> [1.0, 1.5, 2.0, 2.5, 3.0]
```

## 本专题要点
- Top K 不一定非用堆：值的范围有上限时，**桶排序**能做到 O(n)。
- 动态中位数 = **大顶堆（小的一半）+ 小顶堆（大的一半）**，维护顺序和平衡两个条件。
- Python 最大堆：存入 `-x`，取出时再取反。


---

# 全系列总结：Blind 75 知识地图

## 一、Blind 75 是什么

**Blind 75** 是一位 Meta 工程师在匿名职场社区 Blind 上整理的 75 道 LeetCode 精选题，覆盖了面试最常考的数据结构和算法。NeetCode 把每道题都录成了视频，这个播放列表共 75 集，每集讲一道题，总时长约 16.5 小时。

它和"LeetCode 刷题套路系列"（Leetcode18 仓库里的 18 集课程）正好互补：
- **刷题套路系列**：按算法类别讲**模板和方法论**，偏"道"；
- **Blind 75**：每集一道**具体的高频题**，从暴力解讲到最优解，偏"术"。

建议先用刷题套路系列建立框架，再用 Blind 75 大量练习，把模板用到具体题目上。

## 二、75 道题按专题一览

| 专题 | 题数 | 题目 | 核心技巧 |
| --- | --- | --- | --- |
| [数组](notes/01-数组.md) | 10 | 1, 121, 217, 238, 53, 152, 153, 33, 15, 11 | 哈希表、双指针、前缀积、Kadane、旋转数组二分 |
| [位运算](notes/02-位运算.md) | 5 | 191, 338, 268, 190, 371 | `n&1`、`n&(n-1)`、异或抵消、进位 |
| [动态规划](notes/03-动态规划.md) | 11 | 70, 322, 300, 1143, 139, 39, 198, 213, 91, 62, 55 | 决策树 → 缓存 → 填表 → 滚动变量 |
| [图](notes/04-图.md) | 8 | 133, 207, 417, 200, 128, 269, 261, 323 | DFS/BFS + visited、找环、拓扑排序、并查集 |
| [区间](notes/05-区间.md) | 5 | 57, 56, 435, 252, 253 | 按起点排序、贪心、开始结束分别排序 |
| [链表](notes/06-链表.md) | 6 | 206, 141, 21, 23, 19, 143 | 哑结点、快慢指针、反转 |
| [矩阵](notes/07-矩阵.md) | 4 | 73, 54, 48, 79 | 原地标记、边界收缩、四角轮换、网格回溯 |
| [字符串](notes/08-字符串.md) | 10 | 3, 424, 76, 49, 20, 125, 5, 647, 271, 242 | 滑动窗口、频次计数、中心扩展、长度前缀 |
| [树](notes/09-树.md) | 14 | 104, 100, 226, 124, 102, 297, 572, 105, 98, 230, 235, 208, 211, 212 | 递归、BFS、BST 性质、Trie |
| [堆](notes/10-堆.md) | 2 | 347, 295 | 桶排序、双堆 |

## 三、看到什么，想到什么

| 题目特征 | 首先想到 | 代表题 |
| --- | --- | --- |
| 找"另一个数"、判断是否出现过 | 哈希表 / 集合 | 1, 217, 128, 242 |
| 有序数组、两端逼近 | 相向双指针 | 15, 11, 125 |
| 最长 / 最短的**连续**子串、子数组 | 滑动窗口 | 3, 424, 76, 121 |
| 要求 O(log n)，或者数组"原本有序" | 二分查找 | 153, 33 |
| 求最优值，且有重复子问题 | 动态规划 | 70, 322, 300, 1143, 198 |
| 列出所有方案 / 组合 / 路径 | 回溯（选或不选，回溯时撤销） | 39, 79, 212 |
| 依赖关系、先后顺序 | 有向图 + 找环 / 拓扑排序 | 207, 269 |
| 连通块、网格里的"岛" | DFS / BFS 染色，或者并查集 | 200, 323, 417 |
| 区间重叠 | 按起点排序 | 56, 57, 435, 253 |
| 链表找中点、判环、倒数第 k 个 | 快慢指针 | 141, 19, 143 |
| Top K、动态最值、中位数 | 堆（或者桶排序） | 347, 295, 23 |
| 字符串前缀、批量单词查找 | Trie | 208, 211, 212 |
| 回文 | 双指针 / 中心扩展 | 125, 5, 647 |
| 二叉搜索树 | 中序有序、取值范围往下传 | 98, 230, 235 |

## 四、NeetCode 的解题方法

几乎每一集都遵循同样的流程，面试时也可以直接照着讲：
1. **复述题意，看例子**，确认输入输出和边界情况（空数组、重复元素、负数……）；
2. **先说暴力解**，并给出它的复杂度。不要一上来就写最优解，暴力解是你和面试官对齐思路的起点；
3. **找到暴力解里的浪费**：重复计算（→ DP / 缓存）、重复查找（→ 哈希表）、没有用上有序性（→ 二分 / 双指针）；
4. **画图推演**最优解，用例子走一遍，确认每种情况都考虑到了；
5. **写代码**，然后用例子在脑子里跑一遍；
6. **说出时间和空间复杂度**。

## 五、易错点清单

| 易错点 | 题目 |
| --- | --- |
| 股票题发现更低价格时，左指针应该直接跳到右指针的位置 | 121 |
| 乘积子数组要**同时**维护最大积和最小积 | 152 |
| 最大值初值设成 0，导致全是负数时出错 | 53, 124 |
| 三数之和忘了去重（第一个数和左指针都要跳过重复值） | 15 |
| 零钱兑换用贪心会出错 | 322 |
| 打家劫舍 II 只有一间房时没有特殊处理 | 213 |
| 解码方法中 `'0'` 不能单独解码 | 91 |
| 无向图找环时把父结点当成了环 | 261 |
| 合并区间时终点没取 max | 56 |
| 反转链表前没有先保存 `next` | 206, 143 |
| 矩阵置零时边扫边改，或者标记的处理顺序错了 | 73 |
| 螺旋矩阵只剩一行或一列时重复加入 | 54 |
| 验证 BST 只比较了父子结点 | 98 |
| Trie 的 `search` 忘了检查 `end_of_word` | 208 |
| Python 做位运算没有处理负数和 32 位上限 | 371 |

## 六、和第一个系列的对应关系

| Blind 75 专题 | 对应《刷题套路系列》的集数 |
| --- | --- |
| 数组：双指针 / 二分 | 第 2 集（双指针）、第 3 集（二分查找） |
| 链表 | 第 4 集 |
| 字符串：括号 | 第 5 集（栈） |
| 堆 | 第 6 集 |
| 哈希表相关 | 第 7 集 |
| 树 | 第 8 集（BFS）、第 9 集（DFS） |
| 图 | 第 10～12 集 |
| 动态规划 | 第 13～17 集 |
| 回溯（39、79、212） | 第 18 集 |
