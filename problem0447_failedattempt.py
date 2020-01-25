# This attempt fails because the time limit is exceeded
import math
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                
                for k in range(len(points)):
                    if i == k or j == k:
                        continue
                    
                    t1 = (points[i][0], points[i][1])
                    t2 = (points[j][0], points[j][1])
                    t3 = (points[k][0], points[k][1])

                    d_ij = self.distance(t1, t2)
                    d_ik = self.distance(t1, t3)

                    if d_ij == d_ik:
                        n += 1
        return n
                     
    def distance(self, t1, t2):
        return math.sqrt((t1[0] - t2[0])**2 + (t1[1] - t2[1])**2)
