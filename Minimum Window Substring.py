'''
Minimum Window Substring: Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the window. If there is no
such substring, return the empty string "".

The testcases will be generated such that the answer is unique.


Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)
        required = len(t_count)

        left, right = 0, 0
        formed = 0
        window_counts = defaultdict(int)

        min_window = float('inf'), None, None

        while right < len(s):
            char = s[right]
            window_counts[char] += 1

            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1

            while left <= right and formed==required:
                if right-left+1 < min_window[0]:
                    min_window = (right-left+1,left, right)

                left_char = s[left]
                window_counts[left_char] -= 1

                if left_char in t_count and window_counts[left_char] < t_count[left_char]:
                    formed -= 1
                left += 1
            right += 1

        if min_window[0] == float('inf'):
            return ""

        return s[min_window[1]:min_window[2]+1]

sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(sol.minWindow(s,t))