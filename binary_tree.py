from model import *

def IsMember(P, X):
    if IsTreeEmpty(P):
        return False
    else:
        if Root(P) == X:
            return True
        else:
            return IsMember(Left(P) , X) or IsMember(Right(P), X)
        
def IsSkewLeft(P):
    if IsTreeEmpty(P):
        return False
    else:
        if IsOneElmt(P):
            return True
        elif not(IsUnerLeft(P)):
            return False
        else:
            return IsSkewLeft(Left(P))
        
def IsSkewRight(P):
    if IsTreeEmpty(P):
        return False
    else:
        if IsOneElmt(P):
            return True
        elif not(IsUnerRight(P)):
            return False
        else:
            return IsSkewRight(Right(P))
        
def LevelOfX(P, X):
    if not(IsMember(P, X)):
        return None
    else:
        if Root(P) == X:
            return 0
        else:
            if IsBiner(P):
                if IsMember(Left(P), X):
                    return 1 + LevelOfX(Left(P), X)
                elif IsMember(Right(P), X):
                    return 1 + LevelOfX(Right(P), X)
            elif IsUnerLeft(P):
                if IsMember(Left(P), X):
                    return 1 + LevelOfX(Left(P), X)
            elif IsUnerRight(P):
                if IsMember(Right(P), X):
                    return 1 + LevelOfX(Right(P), X)

# P = MakeT(2, MakeT(3, MakeT(4, MakeT(5))))
# P = MakeT(2,None, MakeT(3, None, MakeT(4, None,MakeT(5))))
# P = MakeT(2,MakeT(7), MakeT(3, MakeT(9), MakeT(4, MakeT(5))))
# P = MakeT(2,MakeT(7), MakeT(3, MakeT(9), MakeT(4, None,MakeT(5))))
# P = MakeT(4, MakeT(5), None)
# X = 10

# print(IsExistLeft(P))
# print(IsMember(P, X))
# print(IsSkewLeft(P))
# print(IsSkewLeft(P))
# print(IsSkewRight(P))
# print(LevelOfX(P, X))
# print(IsBiner(P))