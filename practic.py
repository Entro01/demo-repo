def flippingMatrix(matrix):
    print(matrix)

    for i in range(len(matrix)):
        count1 = 0
        count2 = 0
        for j in range(len(matrix)):
            if j < len(matrix)//2:
                count1 += matrix[i][j]
            else:
                count2 += matrix[i][j]
        if count2 > count1:
            for j in range(len(matrix)//2):
                matrix[i][j], matrix[i][len(matrix) - j - 1] = matrix[i][len(matrix) - j - 1], matrix[i][j]

    print(matrix)

    for i in range(len(matrix)):
        count1 = 0
        count2 = 0
        for j in range(len(matrix)):
            if j < len(matrix)//2:
                count1 += matrix[j][i]
            else:
                count2 += matrix[j][i]
        if count2 > count1:
            for j in range(len(matrix)//2):
                matrix[j][i], matrix[len(matrix) - j - 1][i] = matrix[len(matrix) - j - 1][i], matrix[j][i]
    print(matrix)
    
    sum = 0
    for i in range(len(matrix)//2):
        for j in range(len(matrix)//2):
            sum += matrix[i][j]
    
   

    return sum

    

if __name__ == '__main__':
    matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
    print(flippingMatrix(matrix))