def uniquePaths(m, n):
    aux = [[1 for x in range(n)] for x in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            aux[i][j] = aux[i][j-1]+aux[i-1][j]
    for x in aux:
        print(x)
    return aux[-1][-1]

uniquePaths(3, 4)