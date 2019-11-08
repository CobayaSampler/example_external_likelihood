from scipy.stats import norm
from cobaya.likelihood import Likelihood


class test_like2(Likelihood):

    def initialize(self):
        self.norm = norm(loc=self.H0, scale=self.H0_std)

    def add_theory(self):
        self.theory.needs(H0=None)

    def logp(self, **params_values):
        H0_theory = self.theory.get_param("H0")
        return self.norm.logpdf(H0_theory)
