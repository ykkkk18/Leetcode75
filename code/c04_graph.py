"""Blind 75 · 专题 4：图 Graph（第 26～33 集）"""
import sys
from collections import defaultdict, deque
from typing import List

sys.setrecursionlimit(10000)


# ---------- 133. 克隆图 ----------
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


# ---------- 207. 课程表 ----------
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


# ---------- 417. 太平洋大西洋水流问题 ----------
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


# ---------- 200. 岛屿数量 ----------
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


# ---------- 128. 最长连续序列 ----------
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


# ---------- 269. 火星词典（拓扑排序，LeetCode 会员题） ----------
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


# ---------- 261. 以图判树（LeetCode 会员题） ----------
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


# ---------- 323. 无向图中连通分量的数目（并查集，LeetCode 会员题） ----------
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


if __name__ == "__main__":
    # 133：1-2-3-4-1 的环
    ns = [Node(i) for i in range(1, 5)]
    for i, j in ((0, 1), (1, 2), (2, 3), (3, 0)):
        ns[i].neighbors.append(ns[j]); ns[j].neighbors.append(ns[i])
    c = clone_graph(ns[0])
    print("133  clone_graph(四个结点的环) -> 新结点", c.val, "的邻居", [x.val for x in c.neighbors],
          "| 是新对象:", c is not ns[0])
    print("207  can_finish(2, [[1,0]]) ->", can_finish(2, [[1, 0]]), "| (2, [[1,0],[0,1]]) ->", can_finish(2, [[1, 0], [0, 1]]))
    h = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    print("417  pacific_atlantic(示例) ->", pacific_atlantic(h))
    g = [list("11000"), list("11000"), list("00100"), list("00011")]
    print("200  num_islands(示例2) ->", num_islands(g))
    print("128  longest_consecutive([100,4,200,1,3,2]) ->", longest_consecutive([100, 4, 200, 1, 3, 2]))
    print("269  alien_order(['wrt','wrf','er','ett','rftt']) ->", alien_order(["wrt", "wrf", "er", "ett", "rftt"]),
          "| ['z','x','z'] ->", repr(alien_order(["z", "x", "z"])), "| ['abc','ab'] ->", repr(alien_order(["abc", "ab"])))
    print("261  valid_tree(5, [[0,1],[0,2],[0,3],[1,4]]) ->", valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]),
          "| 有环 ->", valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
    print("323  count_components(5, [[0,1],[1,2],[3,4]]) ->", count_components(5, [[0, 1], [1, 2], [3, 4]]))
