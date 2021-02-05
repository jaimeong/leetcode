# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def traverseLL(head):
	print(head.val) 
	head = head.next
	if head != None:
		traverseLL(head)
	else:
		return

# approach 1: dictionary
# time: O(n) 
# space: O(n)
# mydict = {} 
# traverse LL:
#		if currnode not in mydict:
#			add it
#		else:
#			return False 
#
#	return True

# approach 2: floyd's tortoise and hare
# time complexity: o(n)
# space complexity: O(1)

def hasCycle(head) -> bool:
	slow = head 
	fast = head.next

	while(fast.next != None):
		print(slow.val, fast.val)
		if(slow == fast):
			return True

		slow = slow.next 
		fast = fast.next.next

	return False


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node1

node6 = ListNode(6)
node7 = ListNode(7)

node6.next = node7

print(hasCycle(node1))
print(hasCycle(node6))
# traverseLL(node1)
# traverseLL(node6)