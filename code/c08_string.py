"""Blind 75 · 专题 8：字符串 String（第 49～57 集 + 第 74 集）"""
from collections import defaultdict
from typing import List


# ---------- 3. 无重复字符的最长子串 ----------
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


# ---------- 424. 替换后的最长重复字符 ----------
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


# ---------- 76. 最小覆盖子串（Hard） ----------
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


# ---------- 49. 字母异位词分组 ----------
# key = 26 个字母的计数（元组），O(m * n)，比排序 O(m * n log n) 更快
def group_anagrams(strs: List[str]) -> List[List[str]]:
    ans = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)          # list 不能当 key，要转成 tuple
    return list(ans.values())


# ---------- 20. 有效的括号 ----------
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


# ---------- 125. 验证回文串 ----------
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


# ---------- 5. 最长回文子串 ----------
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


# ---------- 647. 回文子串 ----------
# 和第 5 题同一个中心扩展，只是每扩展成功一次就计数 +1
def count_substrings(s: str) -> int:
    res = 0
    for i in range(len(s)):
        for l, r in ((i, i), (i, i + 1)):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l, r = l - 1, r + 1
    return res


# ---------- 271. 字符串的编码与解码（LeetCode 会员题） ----------
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


# ---------- 242. 有效的字母异位词（第 74 集） ----------
# 两个哈希表计数比较；也可以 sorted(s) == sorted(t)（空间更省，时间 O(n log n)）
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count_s, count_t = {}, {}
    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
    return count_s == count_t


if __name__ == "__main__":
    print("3   length_of_longest_substring('abcabcbb') ->", length_of_longest_substring("abcabcbb"),
          "| 'pwwkew' ->", length_of_longest_substring("pwwkew"))
    print("424 character_replacement('ABAB', 2) ->", character_replacement("ABAB", 2),
          "| ('AABABBA', 1) ->", character_replacement("AABABBA", 1))
    print("76  min_window('ADOBECODEBANC', 'ABC') ->", repr(min_window("ADOBECODEBANC", "ABC")),
          "| ('a', 'aa') ->", repr(min_window("a", "aa")))
    print("49  group_anagrams(['eat','tea','tan','ate','nat','bat']) ->",
          group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print("20  is_valid('()[]{}') ->", is_valid("()[]{}"), "| '([)]' ->", is_valid("([)]"), "| '{[]}' ->", is_valid("{[]}"))
    print("125 is_palindrome('A man, a plan, a canal: Panama') ->", is_palindrome("A man, a plan, a canal: Panama"),
          "| 'race a car' ->", is_palindrome("race a car"))
    print("5   longest_palindrome('babad') ->", repr(longest_palindrome("babad")), "| 'cbbd' ->", repr(longest_palindrome("cbbd")))
    print("647 count_substrings('abc') ->", count_substrings("abc"), "| 'aaa' ->", count_substrings("aaa"))
    data = ["neet", "co#de", "", "4#x"]
    enc = encode(data)
    print("271 encode(['neet','co#de','','4#x']) ->", repr(enc), "| decode 回来 ->", decode(enc))
    print("242 is_anagram('anagram', 'nagaram') ->", is_anagram("anagram", "nagaram"), "| ('rat', 'car') ->", is_anagram("rat", "car"))
