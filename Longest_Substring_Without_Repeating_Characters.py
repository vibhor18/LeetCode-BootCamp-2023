class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        left = 0
        hashSet = set()
        
        for right in range(len(s)):
            while s[right] in hashSet:
                hashSet.remove(s[left])
                left += 1
            hashSet.add(s[right])
            count = max(count, right - left + 1)
        return count

        