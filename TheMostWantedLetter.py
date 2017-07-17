def checkio(text):
    d = dict()
    for c in text.lower():
        if c.isalpha():
           if ord(c) not in d:
             d[ord(c)] = 1
           else:
             d[ord(c)] += 1
    l = list(d.keys())    
    l.sort()
    p=d[l[0]]
    s = chr(l[0])
    for i in l:       
       if d[i] > p:
         p= d[i]
         s=chr(i)
    return s
