from .Distance import Distance

class NearestNeighbour(Distance):

    def __init__(self):
        super(NearestNeighbour, self).__init__()


    def NearestNeighbour(self, Z, noCons):
        minEq = float('inf')
        minDis = float('inf')

        distanceFunction = self.cosineSimilarity

        for i in range(len(Z)):
            if i == noCons:
                continue

                    #same label
            if Z[i][1] == Z[noCons][1]:
                t = distanceFunction(Z[i][0], Z[noCons][0])
                if t < minEq:
                    minEq = t
                else:
                    t = distanceFunction(Z[i][0], Z[noCons][0])
                    if t < minDis:
                        minDis = t

        if minDis == 0:
            if minEq == 0:
                return 0
            else:
                return float('inf')

        return float(minEq)/minDis
