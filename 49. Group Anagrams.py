"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""


def groupAnagrams(strs): 
	if len(strs) == 0:
		return [[""]]

	d = {}
	for s in strs:
		sorted_s = "".join(sorted(s))
		if sorted_s in d:
			d[sorted_s].append(s)
		else:
			d[sorted_s] = [s]
		
	return [d[key] for key in d]



print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))




