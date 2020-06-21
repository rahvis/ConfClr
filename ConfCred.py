import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

class ConfCred:
    def __init__(self):
        pass
    
    def plotConfCred(self,x,y):
        c, status, cf = [], [], []
        f, n = 'Failed', 'Normal'
        for a,b in zip(x,y):
            if a < b:
                status.append(n)
                c.append(b)
                d = 1-a
                cf.append(d)

            elif a > b:
                status.append(f)
                c.append(a)
                d = 1-a
                cf.append(d)

        res = {'Credibility':c , 'Confidence':cf}        
        figure(num=None, figsize=(8, 6), dpi=100, facecolor='w', edgecolor='k')
        plt.scatter(cf,c)
        plt.yscale('log')
        plt.xscale('log')
        plt.grid(True)
        plt.title('Uncertainty Estimation of each new prediction')
        plt.xlabel('Confidence')
        plt.ylabel('Credibility')