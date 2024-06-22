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
        plt.plot(q_range, q1_reactions, label='Best Response of Firm 1 (q1 to q2)')
        plt.plot(q2_reactions, q_range, label='Best Response of Firm 2 (q2 to q1)')
        equilibrium = self.find_nash_equilibrium()
        plt.plot(equilibrium[1], equilibrium[0], 'ro', label='Nash Equilibrium')
        plt.xlabel('Quantity by Firm 2')
        plt.ylabel('Quantity by Firm 1')
        plt.title('Cournot Model Best Response Functions and Nash Equilibrium')
        plt.legend()
        plt.grid(True)
        plt.show()

class NCournotModel:
    def __init__(self, a, costs):
        """
        Initialize the n-firm Cournot model with the market intercept and marginal costs for each firm.

        Parameters:
        a (float): Market demand intercept.
        costs (list of floats): Marginal costs for each firm.
        """
        self.a = a
        self.costs = costs
        self.n = len(costs)

    def demand_price(self, quantities):
        """Calculate the market price given quantities by all firms."""
        return self.a - sum(quantities)

    def profit(self, i, quantities):
        """Calculate the profit for firm i."""
        price = self.demand_price(quantities)
        return (price - self.costs[i]) * quantities[i]

    def best_response(self, i, quantities):
        """Calculate firm i's best response given other firms' quantities."""
        other_output = sum(quantities) - quantities[i]
        return max((self.a - self.costs[i] - other_output) / (self.n + 1), 0)

    def find_nash_equilibrium(self, initial_guesses):
        """Find the Nash equilibrium using numerical methods."""
        from scipy.optimize import fsolve

        def equations(quantities):
            return [quantities[i] - self.best_response(i, quantities) for i in range(self.n)]

        equilibrium_quantities = fsolve(equations, initial_guesses)
        return equilibrium_quantities
    
    def plot_equilibrium_quantities(self, quantities):
        """Plot the equilibrium quantities for each firm along with their marginal costs."""
        
        fig, ax = plt.subplots()
        indices = range(len(quantities))
        ax.bar(indices, quantities, color='blue', label='Equilibrium Quantities')

        # Adding a line plot for marginal costs
        ax2 = ax.twinx()  # Create a second y-axis for the marginal costs
        ax2.plot(indices, self.costs, color='red', label='Marginal Costs', marker='o')
        ax2.set_ylabel('Marginal Costs')

        # Setting labels and titles
        ax.set_xlabel('Firms')
        ax.set_ylabel('Quantities')
        ax.set_title('Equilibrium Quantities and Marginal Costs for Each Firm')
        ax.set_xticks(indices)
        ax.set_xticklabels([f'Firm {i+1}' for i in indices])

        # Adding legends for both quantities and costs
        lines, labels = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax2.legend(lines + lines2, labels + labels2, loc='upper left')

        plt.show()
