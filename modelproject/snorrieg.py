from types import SimpleNamespace
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

class CournotModel:
    def __init__(self, a, c1, c2):
        """
        Initialize the Cournot duopoly model with the market intercept and marginal costs for two firms.

        Parameters:
        a (float): Market demand intercept.
        c1 (float): Marginal cost for firm 1.
        c2 (float): Marginal cost for firm 2.
        """
        self.params = SimpleNamespace(a=a, c1=c1, c2=c2)

    def demand_price(self, q1, q2):
        """Calculate the market price given quantities q1 and q2."""
        return self.params.a - q1 - q2

    def profit1(self, q1, q2):
        """Calculate the profit for firm 1."""
        price = self.demand_price(q1, q2)
        return (price - self.params.c1) * q1

    def profit2(self, q1, q2):
        """Calculate the profit for firm 2."""
        price = self.demand_price(q1, q2)
        return (price - self.params.c2) * q2

    def reaction1(self, q2):
        """Calculate firm 1's best response to firm 2's quantity q2."""
        return (self.params.a - self.params.c1 - q2) / 2

    def reaction2(self, q1):
        """Calculate firm 2's best response to firm 1's quantity q1."""
        return (self.params.a - self.params.c2 - q1) / 2

    def find_nash_equilibrium(self):
        """Find the Nash equilibrium using numerical methods."""
        def equations(p):
            q1, q2 = p
            return [q1 - self.reaction1(q2), q2 - self.reaction2(q1)]

        initial_guess = [0, 0]
        equilibrium_quantities = fsolve(equations, initial_guess)
        return equilibrium_quantities
    
    def plot_model(self):
        q_range = np.linspace(0, self.params.a - max(self.params.c1, self.params.c2), 100)
        q1_reactions = [self.reaction1(q) for q in q_range]
        q2_reactions = [self.reaction2(q) for q in q_range]

        plt.figure(figsize=(8, 6))
        plt.plot(q_range, q1_reactions, label='Reaction of Firm 1 (q1 to q2)')
        plt.plot(q2_reactions, q_range, label='Reaction of Firm 2 (q2 to q1)')
        equilibrium = self.find_nash_equilibrium()
        plt.plot(equilibrium[0], equilibrium[1], 'ro', label='Nash Equilibrium')
        plt.xlabel('Quantity by Firm 2')
        plt.ylabel('Quantity by Firm 1')
        plt.title('Cournot Model Reaction Functions and Nash Equilibrium')
        plt.legend()
        plt.grid(True)
        plt.show()