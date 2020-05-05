import math

def divide(iterable,length=None,parts=None,):
    iterable = list(iterable)
    if parts==None:
        parts = math.ceil(len(iterable)/length)
    if length==None:
        length = len(iterable)//parts
    new = []
    for i in range(0,len(iterable),length):
        new.append(iterable[i:i+length])
    return new


def count(iterable):
    iterable = list(iterable)
    d={}
    for item in set(iterable):
        d[item]=iterable.count(item)
    return d

def round(no):
    remainder = no-int(no)
    if remainder>=0.5:
        return math.ceil(no)
    else:
        return math.floor(no)


def sort(iterable,para=None,descending=False):
    for i in range(len(iterable)-1):
        for j in range(i+1,len(iterable)):
            if not descending:
                if getattr(iterable[i],para) > getattr(iterable[j],para):
                    iterable[i],iterable[j] = iterable[j],iterable[i]
            else:
                if getattr(iterable[i],para) < getattr(iterable[j],para):
                    iterable[i],iterable[j] = iterable[j],iterable[i]
    return iterable
