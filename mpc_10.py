import osqp
import scipy.sparse as spa
class MPC10:
    def __init__(self, Ad, Bd, N=10, Q=1, R=0.01):
        self.Ad, self.Bd, self.N = Ad, Bd, N
        self.nx, self.nu = Ad.shape[0], Bd.shape[1]
        self.build_qp(Q, R)
    def build_qp(self, Q, R):

        pass
    def solve(self, x0, xref):

        pass