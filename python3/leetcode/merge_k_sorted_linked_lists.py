# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional

class Solution:
    def length(self, node: ListNode) -> int:
        counter = 1
        while node.next != None:
            node = node.next
            counter += 1
        return counter

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ret_val: Optional[ListNode] = None

        total_count = 0
        for i, node in enumerate(lists):
            if node:
                total_count += self.length(node)
            

        print(total_count)
        # Loop while lists isn't empty
        for _ in range(total_count):
            smallest = 999999
            x = -1
            pop_list = []
            for i, list_node in enumerate(lists):
                # Find the next smallest node value
                if list_node:

                    if list_node.val <= smallest:
                        smallest = list_node.val
                        x = i
                else:
                    # If a "ListNode" is None
                    pop_list.append(i)
            


            curr_node = ret_val
            if curr_node:
                while curr_node.next != None:
                    curr_node = curr_node.next

                curr_node.next = lists[x]
                lists[x] = lists[x].next
                curr_node.next.next = None

            elif lists[x]:
                ret_val = lists[x]
                lists[x] = lists[x].next
                ret_val.next = None

            for i in pop_list[::-1]:
                lists.pop(i)

        return ret_val
    

if __name__ == "__main__":
    def build_linked_list(arr):
        head = ListNode(0)
        curr = head
        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next
        return head.next

    lists = [[1,4,5],[1,3,4],[2,6]]
    #lists = [[],[1]]
    #lists = [[2],[],[-1]]
    linked_lists = [build_linked_list(l) for l in lists]
    solution = Solution()
    result = solution.mergeKLists(linked_lists)
    # Print the merged linked list
    while result:
        print(result.val, end=" ")
        result = result.next