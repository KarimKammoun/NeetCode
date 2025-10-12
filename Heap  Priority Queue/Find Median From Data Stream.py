import heapq

class MedianFinder:

    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.minHeap = []  
        self.maxHeap = [] 

    def addNum(self, num: int) -> None:
        if self.n1 == 0:
            heapq.heappush(self.maxHeap, -num)
            self.n1 += 1
            return

        if self.n2 == 0:
            heapq.heappush(self.minHeap, num)
            self.n2 += 1
            return

        if -self.maxHeap[0] > self.minHeap[0]:
            ox1 = heapq.heappop(self.minHeap)
            ox2 = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, ox2)
            heapq.heappush(self.maxHeap, -ox1)

        if num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
            self.n1 += 1
        else:
            heapq.heappush(self.minHeap, num)
            self.n2 += 1

        if self.n1 > self.n2 + 1:
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
            self.n1 -= 1
            self.n2 += 1
        elif self.n2 > self.n1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)
            self.n2 -= 1
            self.n1 += 1

    def findMedian(self) -> float:
        if self.n1 > self.n2:
            return -self.maxHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0]) / 2
