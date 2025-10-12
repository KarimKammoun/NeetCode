from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.followers = {}      
        self.posts = {}           
        self.time = 0           

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []
        self.posts[userId].insert(0, (self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = {userId}
        
        for i in self.followers.get(userId, []):
            users.add(i)

        for i in users:
            if i in self.posts:
                k=0
                
                for j in self.posts[i]:
                    if k==10:
                        break
                    heapq.heappush(heap, j)
                    k=k+1

        res = []
        for _ in range(10):
            if not heap:
                break
            res.append(heapq.heappop(heap)[1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].discard(followeeId)
