def checkio(data):
    l = list(data)
    my_dict = {i: l.count(i) for i in l}
    res=list()
    for item in l:
        if my_dict[item]>1:
           res.append(item)
    return res
