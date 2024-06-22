from types import SimpleNamespace

class ExchangeEconomyClass:

    def __init__(self):

        par = self.par = SimpleNamespace()

        # a. preferences
        par.alpha = 1/3
        par.beta = 2/3

        # b. endowments
        par.w1A = 0.8
        par.w2A = 0.3

    def utility_A(self,x1A,x2A):
        return x1A**self.par.alpha * x2A**(1-self.par.alpha)

    def utility_B(self,x1B,x2B):
        return x1B**self.par.beta * x2B**(1-self.par.beta)

    def demand_A(self, p1, p2=1):
        par = self.par
        I = p1*par.w1A + p2*par.w2A  # Total income for A
        x1A_star = min(max(par.alpha * I / p1, 0), 1)  # Ensure x1A is between 0 and 1
        x2A_star = min(max((1 - par.alpha) * I / p2, 0), 1)  # Ensure x2A is between 0 and 1
        return x1A_star, x2A_star

    def demand_B(self,p1,p2=1):
        par = self.par
        I = p1*(1 - par.w1A) + p2*(1 - par.w2A)  # Total income for B
        x1B_star = min(max(par.beta * I / p1, 0), 1) # Ensure x1B is between 0 and 1
        x2B_star = min(max((1 - par.beta) * I / p2, 0), 1) # Ensure x2B is between 0 and 1
        return x1B_star, x2B_star

    def check_market_clearing(self,p1,p2=1):

        par = self.par

        x1A,x2A = self.demand_A(p1)
        x1B,x2B = self.demand_B(p1)

        eps1 = x1A-par.w1A + x1B-(1-par.w1A)
        eps2 = x2A-par.w2A + x2B-(1-par.w2A)

        return eps1,eps2
    