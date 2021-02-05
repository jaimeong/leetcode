# class Node:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# n1 = Node(3)
# n2 = Node(2)
# n3 = Node(0)
# n4 = Node(-4)
#
#
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n3
#
#
# def twoPointers(head):
#     fast = head.next
#     slow = head
#
#     while(fast != slow):
#         if(fast.next == None or fast == None):
#             return False
#         # print("fast: " + str(fast.val))
#         # print("slow: " + str(slow.val))
#         fast = fast.next.next
#         slow = slow.next
#
#
#     return True
#
#
# #[3,2,1,5,6,4] and k = 2
#
#
# def kthLarge(alist, k):
#     return sorted(alist)[-k]
# # sorted gives time of nlogn
#
#
# print(kthLarge([3,2,1,5,6,4], 2))
#
# print(kthLarge([3,2,3,1,2,4,5,5,6], 4))




def missingNo(alist):
    return sum([i for i in range(len(alist)+1)]) - sum(alist)




print(missingNo([9,6,4,2,3,5,7,0,1]))
