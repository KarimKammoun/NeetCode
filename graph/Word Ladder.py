class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        
        n=len(wordList)
        m=len(beginWord)
        res=n+1
        
        visited={}

        graph={}


        def compare(i,j):
            r=0
            for c in range(m):
                if wordList[i][c] != wordList[j][c]:
                    r=r+1
                if r>1:
                    return False
            if r==1:
                return True
            return False

        for i in range(n):
            visited[wordList[i]]=0
            for j in range(i+1,n):
                if i==j:
                    continue
                test=compare(i,j)
                if test==True:
                    if wordList[i] not in graph:
                        graph[wordList[i]]=set()
                    if wordList[j] not in graph:
                        graph[wordList[j]]=set()
                    
                    graph[wordList[i]].add(wordList[j])
                    graph[wordList[j]].add(wordList[i])


        def dfs(s,lengh):
            nonlocal res

            if s==endWord:
                if lengh<res:
                    res=lengh
                return 0

            if s in graph:
                for i in graph[s]:
                    if visited[i]==1:
                        continue
                    visited[i]=1
                    dfs(i,lengh+1)
                    visited[i]=0






        
        print(graph)
        visited[beginWord]=1
        dfs(beginWord,1)
        

        if res==n+1:
            return 0
        return res



