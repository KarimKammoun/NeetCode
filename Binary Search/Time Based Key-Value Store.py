class TimeMap:

    def __init__(self):
        self.keyStore = {}
    res=[]
        

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key]=[[value,timestamp]]
        else:
            n=len(self.keyStore[key])
            for i in range(n):
                if self.keyStore[key][i][1]>=timestamp:
                    self.keyStore[key].insert(i,[value,timestamp])
                    return 
            self.keyStore[key].append([value,timestamp])
        print (self.keyStore)
        
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""

        l = self.keyStore[key]
        n = len(l)
        p, q = 0, n - 1

        while p <= q:
            mid = (p + q) // 2
            if l[mid][1] == timestamp:
                return l[mid][0]
            elif l[mid][1] < timestamp:
                p = mid + 1
            else:
                q = mid - 1

        if 0 <= q < n:
            return l[q][0]
        return ""




        









