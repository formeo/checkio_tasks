import math

def checkio(a, b, c):

    cos_beta = (b ** 2 + c ** 2 - a ** 2 ) / (2*b*c)
    cos_gamma = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
    cos_alpha = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)

    
    if (cos_beta <=-1) or (cos_gamma <=-1) or (cos_alpha <=-1):
        return [0,0,0]

    angle_alpha = math.degrees(math.acos(cos_alpha))
    angle_beta = math.degrees(math.acos(cos_beta))
    angle_gamma = math.degrees(math.acos(cos_gamma))

    res_list =[]
    res_list.append(round(angle_beta))
    res_list.append(round(angle_gamma))
    res_list.append(round(angle_alpha))
    res_list.sort()
    return res_list

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
