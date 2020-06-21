class NonConformityMeasure:
    def __init__(self):
        pass
    def AvgDist(self, Z, noCons):
        tipo = Z[noCons][1]
        dimV = len(Z[0][0]) #dim of data vectors
        baryCenter = [] #baryCenter vector
        #for x,y,z,...
        for i in xrange(dimV):
            t = 0
            n = 0
            for y in xrange(len(Z)):
                if Z[y][1] != tipo:
                    continue	
                t += Z[y][0][i]
                n += 1
            baryCenter.append( (float(t)/n) )
            #return distanceFunction(baryCenter, self.Z[noCons][0])
        return baryCenter, Z[noCons][0]
