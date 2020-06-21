from .CP import CP
from .NonConformityMeasure import NonConformityMeasure
from .NearestNeighbour import NearestNeighbour
from .Score import Score
from .ConfCred import ConfCred

class ConfClr(CP,NonConformityMeasure,NearestNeighbour,Score,ConfCred):
    def __init__(self):
        super(ConfClr, self).__init__()
        
