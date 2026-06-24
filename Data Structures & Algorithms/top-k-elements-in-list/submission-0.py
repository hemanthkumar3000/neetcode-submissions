class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        item=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        result=[]
        for i in range(k):
            result.append(item[i][0])
        return result        
        