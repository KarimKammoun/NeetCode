class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
      liste = []
      for i in range(len(position)):
          liste.append([position[i], speed[i]])

      liste.sort(reverse=True)

      for i in range(len(position)):
          liste[i] = (target - liste[i][0]) / liste[i][1]

      i = 0
      while i < len(liste) - 1:
          if liste[i] >= liste[i + 1]: 
              liste.pop(i + 1) 
          else:
              i += 1 
      return(len(liste))