# 1.1 Implement an algorithm to determine if a string has all unique characters. What if you
# can not use additional data structures?

# def uniqueChars1(str):
#     mydict = {}
#     for each in str:
#         if each not in mydict:
#             mydict[each] = 1
#         else:
#             mydict[each] += 1
#     if len(mydict)  == len(str):
#         return True
#     else:
#         return False
#
# print(uniqueChars1("bobert"))
# print(uniqueChars1("chars"))
# print(uniqueChars1("bb"))


# def uniqueChars2(str):
#     for each in str:
#         str.remove(each)
#         if each in str:
#             return False
#     return True
#
#
#
# print(uniqueChars2("bobert"))
# print(uniqueChars2("chars"))
# print(uniqueChars2("bb"))



# 1.2 Write code to reverse a C-Style String. (C-String means that “abcd” is represented as
# five characters, including the null character.)

# def cString(str):
#     return " " + str[::-1]

# 1.3 Design an algorithm and write code to remove the duplicate characters in a string
# without using any additional buffer.

# def removeDupes(s):
#     b = ""
#     for each in s:
#         if each not in b:
#             b += each
#     return b
#
# print(removeDupes("Apple"))

# Write a method to decide if two strings are anagrams or not
# def isAnagram(s1, s2):
#     if len(s1) != len(s2):
#         return False
#     s1 = list(s1)
#     s2 = list(s2)
#
#     for each in s1:
#         if each in s2:
#             s2.remove(each)
#         else:
#             return False
#
#     if s2 == []:
#         return True
#     else:
#         return False
#
# print(isAnagram("racecar", "racecer"))









