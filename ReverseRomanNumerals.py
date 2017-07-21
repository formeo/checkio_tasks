def reverse_roman(data):
   romanic_prev={'CM':900,'CD':400,'XC':90,'XL':40,'IX':9,'IV':4}
   romanic = {'M':1000,'D':500,'C':100,'L':50, 'X':10,'V':5, 'I':1}
   
   for pre_item in romanic_prev:
       if data.find( pre_item ) != -1:
           data=data.replace(pre_item,str(romanic_prev[pre_item])+',')
           
   for item in romanic:
       if data.find( item ) != -1:
           data=data.replace(item,str(romanic[item])+',')
   data=data[0:len(data)-1:1]
   l= [int(x) for x in data.split(',') if x]
   res=0
   for i in l:
       res=res+i
   return res
