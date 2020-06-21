import math


class Distance:

    def __init__(self):
        pass
        
    @staticmethod
    def __testLen(vectorA, vectorB):
        lenA = len(vectorA)
        lenB = len(vectorB)

        if lenA != lenB:
            raise Exception("vectors dimension is different -> A:%d - B:%d"%(lenA, lenB))
        return lenA

    def cosineSimilarity(self, vectorA, vectorB):
        lenV = self.__testLen(vectorA, vectorB)
        numerator = 0
        A2 = 0
        B2 = 0
        for i in range(lenV):
            numerator += vectorA[i] * vectorB[i]
            A2 += vectorA[i]*vectorA[i]
            B2 += vectorB[i]*vectorB[i]

        denominator = math.sqrt(A2*B2)
        if denominator == 0:
            return 2

        return 1 - (float(numerator)/denominator)

    def squaredDistance(self, vectorA, vectorB):
        lenV = self.__testLen(vectorA, vectorB)
        dist = 0
        for i in range(lenV):
            t = vectorA[i] - vectorB[i]
            dist += t*t
        return dist

    def euclideanDistance(self, vectorA, vectorB):
        return math.sqrt(self.squaredDistance(vectorA, vectorB))
