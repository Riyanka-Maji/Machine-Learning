X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]

n = len(X)
sum_x = sum(X)
sum_y = sum(Y)
sum_xy = sum([X[i] * Y[i] for i in range(n)])
sum_x2 = sum([x*x for x in X])

m = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
c = (sum_y - m*sum_x) / n

print("Slope (m):", m)
print("Intercept (c):", c)

def predict(x):
    return m*x + c

print("Prediction for x=6:", predict(6))
