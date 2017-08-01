def flat_list(array):
    if len(array)==0:
        return array
    s=str(array)
    s=s.replace('[','')
    s = s.replace(']', '')
    s=s.strip()
    if s=='':
         return list()
    if s[-1]==',':
        s=s[0:-1:1]
    out_arr =  s.split(',')
    out_arr = list(map(int, out_arr))
    return out_arr
