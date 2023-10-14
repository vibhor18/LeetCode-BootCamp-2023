class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        left = 0
        window_count = {}
        T_count = {}

        for right in t:
            T_count[right] = 1 + T_count.get(right, 0)
        
        have, target = 0, len(T_count)
        result = [-1,-1]
        resLen = float("infinity")

        for right in range(len(s)):
            char = s[right]
            window_count[char] = 1 + window_count.get(char,0)

            if char in T_count and window_count[char] == T_count[char]:
                have += 1
            
            while have == target:
                if (right - left + 1) < resLen:
                    result = [left, right]
                    resLen = right - left + 1
                window_count[s[left]] -= 1
                if s[left] in T_count and window_count[s[left]] < T_count[s[left]]:
                    have -= 1
                left += 1
        left,right = result
        return s[left : right + 1] if resLen != float("infinity") else ""