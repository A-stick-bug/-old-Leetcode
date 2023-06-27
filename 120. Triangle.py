def minimumTotal(triangle) -> int:
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]  # left column

            elif j == i:  # right column
                triangle[i][j] += triangle[i-1][j-1]

            else:
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i-1][j])

    return min(triangle[-1])


print(minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
