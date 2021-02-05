# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
Soln # 1: sort, then see if s=t O(nlogn)
return sorted(t) == sorted(s) 

Soln # 2: dictionary, compare counts/push pop O(n). O(n0)
mydict =  {}
for each in word1:
	add to dict 

for each in word2:
	remove from dict 

return if dict is empty or Note
"""
def isAna(s, t):
	mydict = {}

	if len(s) != len(t):
		return False
	elif len(s) == len(t) == 1 and s != t:
		return False

	for each in s:
		if each not in mydict:
			mydict[each] = 1
		else: 
			mydict[each] += 1

	for each in t:
		if each in mydict:
			mydict[each] -= 1

	for each in mydict:
		if mydict[each] != 0:
			return False 

	return True


print(isAna("anagram","naagram"))
print(isAna("anagram","nam"))
print(isAna("ad","bc"))