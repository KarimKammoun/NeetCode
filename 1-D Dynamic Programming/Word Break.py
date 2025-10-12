class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(wordDict)
        dic={}
        visited=[0]*len(s)

        for i in range(n):
            if wordDict[i][0] not in dic:
                dic[wordDict[i][0]]={(wordDict[i],len(wordDict[i]))}
            else:
                dic[wordDict[i][0]].add((wordDict[i],len(wordDict[i])))
        n=len(s)


        def dfs(i):
            nonlocal n


            res=False
            if i==n:
                return True
            
            if visited[i]==1:
                return False


            if s[i] in dic:
                for j in (dic[s[i]]):


                    lengh=j[1]
                    if i+lengh>n or s[i:(i+lengh)]!=j[0]:
                        continue
                    else:
                        res=dfs(i+lengh)
                    if res==True:
                        return True
            visited[i]=1
            return res


        print(dic)


        res=dfs(0)

        return res



        