class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head):
        curr = head
        arr = []
        while curr is not None:
            arr.append(curr.val)
            curr = curr.next
        ans = arr.copy()

        def next_greater():
            st = []
            j = len(ans) - 1
            for i in arr[::-1]:
                while len(st) > 0 and st[-1] <= i:
                    st.pop()
                if not st:
                    ans[j] = -1
                st.append(i)
                j -= 1

        next_greater()
        ans1 = ListNode(0)
        head1 = ans1
        for i, j in zip(arr, ans):
            if i != j:
                temp = ListNode(i)
                head1.next = temp
                head1 = head1.next

        return ans1.next
