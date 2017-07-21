def checkio(data):
    romanic = {1000: 'M', 900:'CM', 500: 'D',400:'CD', 100: 'C', 90:'XC', 50: 'L',40:'XL', 10: 'X',9:'IX', 5: 'V', 4:'IV', 1: 'I'}
    k=list()
    res=""
    it=0
    while data > 0:
      for item in romanic.keys():
        if data/item>=1:
            k.append(item)
            it=item
            break    
      data = data-it
    for i in k:
        res=res+romanic[i]
    return res
