def checkio(first, second):
   list1=first.split(',')
   list2 = second.split(',')
   set1=set(list1)
   set2=set(list2)
   new_set = set1&set2
   if len(new_set)  == 0:
       return ''
   else:
       return ','.join(sorted(new_set))
