'''
Substring with Concatenation of All Words: You are given a string s and an array of strings words. All the strings
of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are
all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any
permutation of words. Return an array of the starting indices of all the concatenated substrings in s. You can
return the answer in any order.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation:
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation:
There is no concatenated substring.

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation:
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

Constraints:
1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
'''

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = {}

        # Count frequency of each word in words
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        result = []

        # Slide over s in windows of total_len
        for i in range(len(s) - total_len + 1):
            seen = {}
            j = 0

            while j < num_words:
                word_start = i + j * word_len
                word = s[word_start:word_start + word_len]

                if word not in word_count:
                    break

                seen[word] = seen.get(word, 0) + 1

                if seen[word] > word_count[word]:
                    break

                j += 1

            if j == num_words:
                result.append(i)

        return result

sol = Solution()
s = "barfoothefoobarman"
words = ["foo","bar"]
print(sol.findSubstring(s, words))