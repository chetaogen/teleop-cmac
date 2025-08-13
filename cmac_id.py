import numpy as np
class CMACID:
    def __init__(self, n_input=12, n_mem=100, c=5, lr=0.01):
        self.mem = np.zeros(n_mem)
        self.c, self.lr = c, lr
    def _hash(self, x):
        return ((x*2654435761) % self.mem.size).astype(int)
    def __call__(self, x):
        idx = self._hash(x[:self.c])
        return self.mem[idx].sum()
    def update(self, x, delta):
        idx = self._hash(x[:self.c])
        self.mem[idx] += self.lr * delta / self.c