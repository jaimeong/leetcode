# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:

# Input: s = ""
# Output: 0


# time complexity: O(n^2)
# space complexity: O(1)

def longestSubstring(s):
    seen = {}
    length = len(s)
    i = 0
    maxsub = 0
    
    for j in range(length):
        if s[j] in seen:
            #readjust pointer to last seen
            i = max(seen[s[j]], i)
            
        maxsub = max(maxsub, j -i + 1)
        #add index to seen
        seen[s[j]] = j + 1
        
    return maxsub



print("----")
print(longestSubstring("abcbba")) #3
print(longestSubstring("abcabcbb")) #3

