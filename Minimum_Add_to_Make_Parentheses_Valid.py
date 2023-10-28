class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        corrections = 0
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            
            if balance < 0:
                corrections += 1
                balance = 0
        
        return corrections + balance
        