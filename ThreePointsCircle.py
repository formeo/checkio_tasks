import math
def checkio(data):

    x1=int(data[1])
    y1=int(data[3])

    x2 = int(data[7])
    y2 = int(data[9])

    x3 = int(data[13])
    y3 = int(data[15])

    A = x2 - x1
    B = y2 - y1
    C = x3 - x1
    D = y3 - y1
    E = A * (x1 + x2) + B * (y1 + y2)
    F = C * (x1 + x3) + D * (y1 + y3)
    G = 2 * (A * (y3 - y2) - B * (x3 - x2))

    h = (D * E - B * F) / G
    k = (A * F - C * E) / G
    r = ((x1 - h) ** 2) + ((y1 - k) ** 2)

    if h.is_integer():
        h=int(h)
        hstr =str(h)
    else:
      hstr=float("{0:.2f}".format(h))    

    if k.is_integer():
        k=int(k)
        kstr =str(k)
    else:
      kstr=float("{0:.2f}".format(k))


    r=math.sqrt(r)
    r=float("{0:.2f}".format(r))
    
    if r.is_integer():
        rstr = int(r)
    else:
        rstr =float("{0:.2f}".format(r))

    return "(x-"+str(hstr)+")^2+(y-"+str(kstr)+")^2="+str(rstr)+"^2"
