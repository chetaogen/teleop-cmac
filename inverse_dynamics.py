import numpy as np
from scipy.linalg import pinv

class InverseDynamics:
    def __init__(self, M, C, G):
        self.M, self.C, self.G = M, C, G
    def torque(self, q, dq, ddq_ref):
        return self.M(q) @ ddq_ref + self.C(q, dq) @ dq + self.G(q)