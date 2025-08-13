from sklearn.neural_network import MLPRegressor
class RBFID:
    def __init__(self, hidden=100):
        self.net = MLPRegressor(hidden_layer_sizes=(hidden,), activation='tanh')
    def fit(self, X, y): self.net.fit(X, y)
    def predict(self, X): return self.net.predict(X)