class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n =0
        r=ListNode(0,None)
        res=r


        def serch():
            k=0
            m=10000

            for i in range(len(lists)):
                if lists[i].val<m:
                    m=lists[i].val
                    k=i
            res=lists[k]
            lists[k]=lists[k].next
            if lists[k]==None:
                lists.pop(k)

            return res




        while (len(lists)>0):
            r.next=serch()
            r=r.next
        
        
        return res.next



        
        