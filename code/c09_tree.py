"""Blind 75 · 专题 9：树 Tree（第 58～71 集）"""
import sys
from collections import deque
from typing import List, Optional

sys.setrecursionlimit(10000)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build_tree(vals):
    """按 LeetCode 层序写法建树：[3,9,20,None,None,15,7]"""
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q, i = deque([root]), 1
    while q and i < len(vals):
        node = q.popleft()
        for side in ("left", "right"):
            if i < len(vals) and vals[i] is not None:
                child = TreeNode(vals[i]); setattr(node, side, child); q.append(child)
            i += 1
    return root


def to_level_list(root):
    out, q = [], deque([root])
    while q:
        node = q.popleft()
        out.append(node.val if node else None)
        if node:
            q.extend([node.left, node.right])
    while out and out[-1] is None:
        out.pop()
    return out


# ---------- 104. 二叉树的最大深度（视频讲了 3 种） ----------
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


# ---------- 100. 相同的树 ----------
def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


# ---------- 226. 翻转二叉树 ----------
def invert_tree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root


# ---------- 124. 二叉树中的最大路径和（Hard） ----------
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


# ---------- 102. 二叉树的层序遍历 ----------
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


# ---------- 297. 二叉树的序列化与反序列化（Hard） ----------
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


# ---------- 572. 另一棵树的子树 ----------
# 对 root 的每个结点，都检查"以它为根的子树"和 sub_root 是否相同（复用 100 题）
def is_subtree(root, sub_root):
    if not sub_root:
        return True
    if not root:
        return False
    if is_same_tree(root, sub_root):
        return True
    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)


# ---------- 105. 从前序与中序遍历序列构造二叉树 ----------
# 前序第一个 = 根；在中序里找到根的位置 mid：左边 mid 个是左子树，右边是右子树
def build_tree_from(preorder: List[int], inorder: List[int]):
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = build_tree_from(preorder[1:mid + 1], inorder[:mid])
    root.right = build_tree_from(preorder[mid + 1:], inorder[mid + 1:])
    return root


# ---------- 98. 验证二叉搜索树 ----------
# 只比较父子不够！要把每个结点允许的取值范围 (left, right) 往下传
def is_valid_bst(root):
    def valid(node, left, right):
        if not node:
            return True
        if not (left < node.val < right):
            return False
        return valid(node.left, left, node.val) and valid(node.right, node.val, right)

    return valid(root, float("-inf"), float("inf"))


# ---------- 230. 二叉搜索树中第 K 小的元素 ----------
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


# ---------- 235. 二叉搜索树的最近公共祖先 ----------
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


# ---------- 208. 实现 Trie（前缀树） ----------
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


# ---------- 211. 添加与搜索单词（支持 '.' 通配符） ----------
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


# ---------- 212. 单词搜索 II（Hard，Trie + 回溯） ----------
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


if __name__ == "__main__":
    t = build_tree([3, 9, 20, None, None, 15, 7])
    print("104 max_depth([3,9,20,null,null,15,7]) -> 递归", max_depth(t), "| BFS", max_depth_bfs(t), "| 迭代DFS", max_depth_iter(t))
    print("100 is_same_tree([1,2,3],[1,2,3]) ->", is_same_tree(build_tree([1, 2, 3]), build_tree([1, 2, 3])),
          "| ([1,2],[1,null,2]) ->", is_same_tree(build_tree([1, 2]), build_tree([1, None, 2])))
    print("226 invert_tree([4,2,7,1,3,6,9]) ->", to_level_list(invert_tree(build_tree([4, 2, 7, 1, 3, 6, 9]))))
    print("124 max_path_sum([-10,9,20,null,null,15,7]) ->", max_path_sum(build_tree([-10, 9, 20, None, None, 15, 7])),
          "| [-3] ->", max_path_sum(build_tree([-3])))
    print("102 level_order([3,9,20,null,null,15,7]) ->", level_order(t))
    s = serialize(build_tree([1, 2, 3, None, None, 4, 5]))
    print("297 serialize([1,2,3,null,null,4,5]) ->", repr(s), "| deserialize 回来 ->", to_level_list(deserialize(s)))
    print("572 is_subtree([3,4,5,1,2],[4,1,2]) ->", is_subtree(build_tree([3, 4, 5, 1, 2]), build_tree([4, 1, 2])),
          "| ([3,4,5,1,2,null,null,null,null,0],[4,1,2]) ->",
          is_subtree(build_tree([3, 4, 5, 1, 2, None, None, None, None, 0]), build_tree([4, 1, 2])))
    print("105 build_tree_from([3,9,20,15,7],[9,3,15,20,7]) ->", to_level_list(build_tree_from([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])))
    print("98  is_valid_bst([2,1,3]) ->", is_valid_bst(build_tree([2, 1, 3])),
          "| [5,1,4,null,null,3,6] ->", is_valid_bst(build_tree([5, 1, 4, None, None, 3, 6])),
          "| [5,4,6,null,null,3,7]（3 在 5 的右子树里）->", is_valid_bst(build_tree([5, 4, 6, None, None, 3, 7])))
    print("230 kth_smallest([5,3,6,2,4,null,null,1], 3) ->", kth_smallest(build_tree([5, 3, 6, 2, 4, None, None, 1]), 3))
    bst = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    print("235 LCA(2, 8) ->", lowest_common_ancestor(bst, TreeNode(2), TreeNode(8)).val,
          "| LCA(2, 4) ->", lowest_common_ancestor(bst, TreeNode(2), TreeNode(4)).val)
    tr = Trie(); tr.insert("apple")
    print("208 Trie: insert apple -> search('apple')", tr.search("apple"), "| search('app')", tr.search("app"),
          "| startsWith('app')", tr.startsWith("app"))
    wd = WordDictionary()
    for w in ("bad", "dad", "mad"):
        wd.addWord(w)
    print("211 search('pad'), ('bad'), ('.ad'), ('b..') ->", wd.search("pad"), wd.search("bad"), wd.search(".ad"), wd.search("b.."))
    board = [list("oaan"), list("etae"), list("ihkr"), list("iflv")]
    print("212 find_words(board, ['oath','pea','eat','rain']) ->", find_words(board, ["oath", "pea", "eat", "rain"]))
