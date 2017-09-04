def checkio(game_result):

    # print(game_result)
    new_list=[]
    for item in game_result:
        new_list.append(list(item))
    # print(new_list)

    for x in range(len(new_list[0])):
        for y in range(len(new_list)):
            if y + 2 <= len(new_list[len(new_list) - 1]) - 1:
                if new_list[x][y] == new_list[x][y + 1] == new_list[x][y + 2]:
                    if new_list[x][y] in('X','O'):
                        return new_list[x][y]

    for x in range(len(new_list[0])):
        for y in range(len(new_list)):
           if x + 2 <= len(new_list[0]) - 1:
               if new_list[x][y] == new_list[x + 1][y] == new_list[x + 2][y]:
                   if new_list[x][y] in('X','O'):
                        return new_list[x][y]

    for x in range(len(new_list[0])):
        for y in range(len(new_list)):               
                if y + 2 <= len(new_list[0]) - 1 and x + 2 <= len(new_list) - 1:
                    if new_list[x][y] == new_list[x + 1][y + 1] == new_list[x + 2][y + 2]:
                        if new_list[x][y] in('X','O'):
                            return new_list[x][y]

                if y >= 2 and len(new_list[0]) - y < 2:
                    if x + 2 <= len(new_list) - 1:
                        if new_list[x][y] == new_list[x + 1][y - 1] == new_list[x + 2][y - 2]:
                            if new_list[x][y] in('X','O'):
                                return new_list[x][y]


    return 'D'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

