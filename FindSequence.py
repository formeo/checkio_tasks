def checkio(matrix):

    if len(matrix) == 1:
        matrix = matrix[0]

    sequence = False

    # horizontal
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
          if y + 3 <= len(matrix[len(matrix) - 1]) - 1:
              if matrix[x][y] == matrix[x][y+1] == matrix[x][y+2] == matrix[x][y+3]:               
                  return True
   
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            if x+3 <= len(matrix[0]) - 1:
                if matrix[x][y]== matrix[x + 1][y] == matrix[x+2][y] == matrix[x+3][y]:                  
                    return True

    
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            #print(y)
            if y==len(matrix[0]) - 1 and x + 3 <= len(matrix) - 1:
                print("matrix[x][y]",matrix[x][y])
                if matrix[x][y] == matrix[x + 1][y - 1] == matrix[x + 2][y - 2] == matrix[x + 3][y - 3]:
                  return True
            if y < 3:
                if y + 3 <= len(matrix[0]) - 1 and x + 3 <= len(matrix) - 1:
                    if matrix[x][y] == matrix[x + 1][y + 1] == matrix[x + 2][y + 2] == matrix[x + 3][y + 3]:
                        return True

            if y >= 4 and len(matrix[0]) - y < 4:
                if x + 3 <= len(matrix) - 1:
                    if matrix[x][y] == matrix[x + 1][y - 1] == matrix[x + 2][y - 2] == matrix[x + 3][y - 3]:
                        return True
            if y >= 4 and len(matrix[0]) - y >= 4:

                if x + 3 <= len(matrix) - 1 and y - 3 >= 0:
                    if matrix[x][y] == matrix[x + 1][y - 1] == matrix[x + 2][y - 2] == matrix[x + 3][y - 3]:
                        return True
                    if matrix[x][y] == matrix[x + 1][y + 1] == matrix[x + 2][y + 2] == matrix[x + 3][y + 3]:
                        return True
    return False
