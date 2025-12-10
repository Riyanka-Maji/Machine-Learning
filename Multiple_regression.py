def multiple_regression(x1, x2, y):

    n = len(x1)
    sum_x1 = 0
    sum_x2 = 0
    sum_y  = 0

    sum_x1_sq = 0
    sum_x2_sq = 0

    sum_x1y = 0
    sum_x2y = 0

    sum_x1x2 = 0
    for i in range(n):
        sum_x1 += x1[i]
        sum_x2 += x2[i]
        sum_y  += y[i]

        sum_x1_sq += x1[i] * x1[i]
        sum_x2_sq += x2[i] * x2[i]

        sum_x1y += x1[i] * y[i]
        sum_x2y += x2[i] * y[i]

        sum_x1x2 += x1[i] * x2[i]

    D = (sum_x1_sq * sum_x2_sq) - (sum_x1x2 ** 2)
    B1 = ((sum_x2_sq * sum_x1y) - (sum_x1x2 * sum_x2y)) / D
    B2 = ((sum_x1_sq * sum_x2y) - (sum_x1x2 * sum_x1y)) / D

    mean_x1 = sum_x1 / n
    mean_x2 = sum_x2 / n
    mean_y  = sum_y  / n
    B0 = mean_y - (B1 * mean_x1) - (B2 * mean_x2)
    return B0, B1, B2

x1 = [3,4,5,6,2]
x2 = [8,5,7,3,1]
y  = [-3.7,3.5,2.5,11.5,5.7]

B0, B1, B2 = multiple_regression(x1, x2, y)
print("B0 =", B0)
print("B1 =", B1)
print("B2 =", B2)
