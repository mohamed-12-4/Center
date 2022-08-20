import numpy as np
"""
class LinearRegression:
    def __init__(self, alpha=0.01, n_iter=100, b=0):
        self.alpha = alpha
        self.n_iter = n_iter
        self.w = None
        self.b = b

    def fit(self, X_train, y):
        self.w = np.zeros(X_train.shape[1], dtype=np.float64)
        for i in range(self.n_iter):
            dw, db = self.compute_gradient(self.w, self.b, X_train, y)
            self.w -= self.alpha * dw
            self.b -= self.alpha * db
            if i % 10 == 0:
                print(self.cost_function(X_train, y, self.w, self.b))

    def cost_function(self, x, y, w, b):
        cost = 0.0
        m = x.shape[0]
        for i in range(x.shape[0]):
            fw_b = np.dot(x[i], w) + b
            cost = cost + (fw_b - y[i])**2

        return cost / 2*m

    def compute_gradient(self, w, b, x, y):
        m = x.shape[0]
        n = x.shape[1]
        db = 0
        dw = np.zeros((n,), dtype=np.float)
        for i in range(m):
            err = (np.dot(x[i], w) + b) - y[i]
            for j in range(n):
                dw[j] = dw[j] + err * x[i, j]
            db += err

        return dw/m, db/m

    def predict(self,x):
        return np.dot(x, w) + self.b
""" 

X_train = np.array([[2104, 5, 1, 45], [1416, 3, 2, 40], [852, 2, 1, 35]])
y_train = np.array([460, 232, 178])


model = LinearRegression(alpha=0.01, n_iter=200)
model.fit(X_train, y_train)