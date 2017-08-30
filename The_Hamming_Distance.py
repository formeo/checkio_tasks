def IntToByte(n):
    b = 2147483648;
    str=''
    while b > 0:
        z = n & b;
        if z == 0:
             str=str+'0'
        else:
             str=str+'1'
        b = b >> 1;
    return str  
  


def checkio(n, m):
  nlist=[int(x) for x in str(IntToByte(n))]
  mlist=[int(x) for x in str(IntToByte(m))]
  res_list=[1 for i,item in enumerate(nlist) if nlist[i] != mlist[i]]
  return sum(res_list)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
