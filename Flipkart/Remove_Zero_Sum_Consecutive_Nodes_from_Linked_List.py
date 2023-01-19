# Runtime = 29ms (90%) 
# Memory = 13.8MB (90%)

class Solution(object):
    def removeZeroSumSublists(self, head):
		prehead = ListNode(0)
		prehead.next = head
		current = head
		sum_map = {0: prehead} 
		cumsum = 0
		while current:
			cumsum += current.val
			if cumsum in sum_map: 
				prevmatch = sum_map[cumsum]
				walker = prevmatch.next
				wsum = cumsum
				while walker != current:
					wsum += walker.val
					del sum_map[wsum] 
					walker = walker.next
				prevmatch.next = current.next
			else:
				sum_map[cumsum] = current
			current = current.next
		return prehead.next