class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = "".join(char.lower() for char in s if char.isalnum())
        left = 0
        right = len(temp) - 1
        while left < right:
            if temp[left] != temp[right]:
                return False
            left += 1
            right -= 1
        return True