class tree:
    def __init__(self, A = None, L = None, R = None):
        self.A = A
        self.L = L
        self.R = R
        
    def __repr__(self):
        return "((%s, %s, %s))" % (repr(self.A), repr(self.L), repr(self.R))
        
def MakeT(A = None, L = None, R = None):
    return tree(A, L, R)

def Root(T):
    return T.A

def Left(T):
    return T.L

def Right(T):
    return T.R

# Model 1
def IsTreeEmpty(T):
    return T == None

def IsOneElmt(T):
    return not(IsTreeEmpty((T))) and IsTreeEmpty(Left(T)) and IsTreeEmpty(Right(T))

def IsUnerLeft(T):
    return not(IsTreeEmpty(Left(T))) and IsTreeEmpty(Right(T))

def IsUnerRight(T):
    return IsTreeEmpty(Left(T)) and not(IsTreeEmpty(Right(T)))

def IsBiner(T):
    if not(IsTreeEmpty(T)):
        return not(IsTreeEmpty(Left(T))) and not(IsTreeEmpty(Right(T)))
    else:
        return False

def IsExistLeft(T):
    if not(IsTreeEmpty(T)):
        return not(IsTreeEmpty(Left(T)))
    else:
        return False

def IsExistRight(T):
    if not(IsTreeEmpty(T)):
        return not(IsTreeEmpty(Right(T)))
    else:
        return False

# Model 0
def NbElmt(T):
    if IsTreeEmpty(T):
        return 0
    else:
        return NbElmt(Right(T)) + NbElmt(Left(T)) + 1
    
def NbDaun(T):
    if IsTreeEmpty(T):
        return 0
    else:
        if IsTreeEmpty(Right(T)) and IsTreeEmpty(Left(T)):
            return 1
        else:
            return NbDaun(Right(T)) + NbDaun(Left(T))
         
def RepPrefix(T):
    if IsOneElmt(T):
        return [Root(T)]
    else:
        if IsBiner(T):
            return [Root(T)] + RepPrefix(Left(T)) + RepPrefix(Right(T)) 
        elif IsUnerRight(T):
            return [Root(T)] + RepPrefix(Right(T)) 
        elif IsUnerLeft(T):
            return  [Root(T)] + RepPrefix(Left(T))
        
# T = MakeT(2,MakeT(3,MakeT(1,None,None),MakeT(5,None,None)),MakeT(3,MakeT(2,None,None),MakeT(4,None,None)))
# T = MakeT(MakeT(1, 2, None), 4, None)
# T = MakeT(None, 5, None)
# T = MakeT(1, 2 , 3)
# T = MakeT(2,MakeT(3,MakeT(1),MakeT(5)),MakeT(3,MakeT(2),MakeT(4)))

# print(NbElmt(T))
# print(RepPrefix(T))
# print(IsUnerLeft(T))
# print(IsExistLeft(T))