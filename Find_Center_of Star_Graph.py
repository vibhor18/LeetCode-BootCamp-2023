class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        temp1 = edges[0]
        temp2 = edges[1]
        if(temp1[0]==temp2[0] or temp1[0]==temp2[1]):
            return temp1[0]
        else:
            return temp1[1]
