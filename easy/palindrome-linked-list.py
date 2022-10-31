class Solution:
    """
    Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
    """
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # We are going to turn the linked list into a string and then check if it's a palindrome.
        word = ""
        item = head
        while item is not None:
            word += str(item.val)
            item = item.next
            
        if word == word[::-1]:
            return True
        return False
