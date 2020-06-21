'''Conformal Prediction
A: nonConformity function
B: training set
z: the test example
'''

class CP:
    def __init__(self):
        self.Alpha = []
        self.pValue = None

    def ConfPred(self, A, error, B, z):
        self.Aalpha = []
        B.append(z)
        n=len(B)
        for i in range(n):
            self.Aalpha.append(A(B, i))
        B.pop(n-1) #restore previus state of B
        c=0

        for i in range(n):
            if self.Aalpha[i] >= self.Aalpha[n-1]:
                c += 1

        self.pValue = float(c)/n
        if self.pValue > error:
            return True, self.pValue
        else:
            return False, self.pValue
