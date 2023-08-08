class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=dic.get(i,0)+1
        print(dic)
        liste=[]
        for i in range(k):
            s=0
            d=0
            for c in dic:
                if dic[c]>s:
                    s=dic[c]
                    d=c
            liste.append(d)
            dic[d]=0
        return liste
    