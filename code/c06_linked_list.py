"""Blind 75 · 专题 6：链表 Linked List（第 39～44 集）"""
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def build(vals):
    dummy = cur = ListNode()
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


# ---------- 206. 反转链表 ----------
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


# ---------- 141. 环形链表（Floyd 龟兔赛跑） ----------
# 快指针每次 2 步，慢指针每次 1 步；有环时每走一轮两者距离缩小 1，必定相遇
def has_cycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False


# ---------- 21. 合并两个有序链表 ----------
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


# ---------- 23. 合并 K 个升序链表 ----------
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


# ---------- 19. 删除链表的倒数第 N 个结点 ----------
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


# ---------- 143. 重排链表 ----------
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


if __name__ == "__main__":
    print("206 reverse_list([1,2,3,4,5]) ->", to_list(reverse_list(build([1, 2, 3, 4, 5]))),
          "| 递归版 ->", to_list(reverse_list_recursive(build([1, 2, 3, 4, 5]))))
    c = build([3, 2, 0, -4]); c.next.next.next.next = c.next
    print("141 has_cycle(3,2,0,-4 尾部连回 2) ->", has_cycle(c), "| [1,2] ->", has_cycle(build([1, 2])))
    print("21  merge_two_lists([1,2,4],[1,3,4]) ->", to_list(merge_two_lists(build([1, 2, 4]), build([1, 3, 4]))))
    print("23  merge_k_lists([1,4,5],[1,3,4],[2,6]) ->",
          to_list(merge_k_lists([build([1, 4, 5]), build([1, 3, 4]), build([2, 6])])),
          "| 堆版 ->", to_list(merge_k_lists_heap([build([1, 4, 5]), build([1, 3, 4]), build([2, 6])])))
    print("19  remove_nth_from_end([1,2,3,4,5], 2) ->", to_list(remove_nth_from_end(build([1, 2, 3, 4, 5]), 2)),
          "| ([1], 1) ->", to_list(remove_nth_from_end(build([1]), 1)))
    for vals in ([1, 2, 3, 4], [1, 2, 3, 4, 5]):
        h = build(vals); reorder_list(h)
        print(f"143 reorder_list({vals}) ->", to_list(h))
