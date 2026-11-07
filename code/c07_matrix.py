"""Blind 75 · 专题 7：矩阵 Matrix（第 45～48 集）"""
from typing import List


# ---------- 73. 矩阵置零 ----------
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


# ---------- 54. 螺旋矩阵 ----------
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


# ---------- 48. 旋转图像 ----------
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


# ---------- 79. 单词搜索（回溯） ----------
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


def show(m):
    return " ".join(str(row) for row in m)


if __name__ == "__main__":
    m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]; set_zeroes(m)
    print("73 set_zeroes([[1,1,1],[1,0,1],[1,1,1]]) ->", show(m))
    m = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]; set_zeroes(m)
    print("73 set_zeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]) ->", show(m))
    print("54 spiral_order(3x3) ->", spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print("54 spiral_order(3x4) ->", spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]; rotate(m)
    m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]; rotate_flip(m2)
    print("48 rotate(3x3) ->", show(m), "| 翻转+转置版 ->", show(m2))
    m = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]; rotate(m)
    print("48 rotate(4x4) ->", show(m))
    b = [list("ABCE"), list("SFCS"), list("ADEE")]
    print("79 exist(board, 'ABCCED') ->", exist(b, "ABCCED"), "| 'SEE' ->", exist(b, "SEE"), "| 'ABCB' ->", exist(b, "ABCB"))
