def min(l):
    min=l[0]
    for x in l:
        if(x<min):
            min=x
    return min

def sort(l):
    m=min(l)
    l.remove(m)
    return [m]+sort(l[1:])

