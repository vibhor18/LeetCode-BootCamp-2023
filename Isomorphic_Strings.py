class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashMap = {}
        for i in range(len(s)):
            if s[i] not in hashMap.keys():
                if t[i] not in hashMap.values():
                    hashMap[s[i]] = t[i]
                else:
                    return False
            else:
                if hashMap[s[i]] == t[i]:
                    continue
                else:
                    return False
        return True
