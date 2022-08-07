import numpy as np

class LinearRegression:
    def __init__(self, alpha=0.01, n_iter=100, w=0, b=0):
        self.alpha = alpha
        self.n_iter = n_iter
        self.w = w
        self.b = b

    def fit(self, x, y):

        for i in range(self.n_iter):
            dw, db = self.compute_gradient(self.w, self.b, x, y)
            self.w -= self.alpha * dw
            self.b -= self.alpha * db
            if i % 10 == 0:
                print(self.cost_function(x, y, self.w, self.b))

    def cost_function(self, x, y, w, b):
        cost = 0
        m = x.shape[0]
        for i in range(x.shape[0]):
            fw_b = w*x[i] + b
            cost += (fw_b - y[i]) ** 2

        return 1/2*m*(cost)

    def compute_gradient(self, w, b, x, y):
        dw, db = 0, 0
        m = x.shape[0]
        for i in range(x.shape[0]):
            fw_b = w*x[i] + b
            dw_i = (fw_b - y[i])*x[i]
            db_i = fw_b - y[i]
            dw += dw_i
            db += db_i

        return dw/m, db/m

    def predict(self,x):
        return x*self.w + self.b

x_train = np.array([1.0, 2.0, 3, 4, 5, 6])   #features
y_train = np.array([300.0, 500.0, 700, 900, 1100, 1300])   #target value

model = LinearRegression(alpha=0.01, n_iter=10000)
model.fit(x_train, y_train)
print(f"Prediction: {model.predict(7)} ") 