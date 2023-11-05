class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums)+1)]
        result  = []
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        for number, c in count.items():
            freq[c].append(number) 

        for i in range(len(freq)-1, 0 , -1):
            for number in freq[i]:
                result.append(number)
                if len(result) == k:
                    return result