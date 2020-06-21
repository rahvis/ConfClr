import pandas as pd

class Score:
    def __init__(self):
        pass

    def conformalScore(self,x,y):
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

        res = {'p-FAILED':x, 'p-NORMAL': y, 'Status':status, 'Credibility':c , 'Confidence':cf}        
        df_r = pd.DataFrame(res, index=None)
        return df_r
