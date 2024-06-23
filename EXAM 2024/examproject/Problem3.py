import numpy as np

class Barycentric:
    def __init__(self, seed=2024):
        self.rng = np.random.default_rng(seed)
        self.X = self.rng.uniform(size=(50, 2))
        self.y = self.rng.uniform(size=(2,))
    
    def find_closest_points(self):
        A = B = C = D = None
        min_dist_A = min_dist_B = min_dist_C = min_dist_D = np.inf

        for point in self.X:
            dist = np.sqrt((point[0] - self.y[0])**2 + (point[1] - self.y[1])**2)
            
            # Check if the point is within the unit square [0, 1] x [0, 1]
            if 0 <= point[0] <= 1 and 0 <= point[1] <= 1:
                if point[0] > self.y[0] and point[1] > self.y[1] and dist < min_dist_A:
                    A = point
                    min_dist_A = dist
                elif point[0] > self.y[0] and point[1] < self.y[1] and dist < min_dist_B:
                    B = point
                    min_dist_B = dist
                elif point[0] < self.y[0] and point[1] < self.y[1] and dist < min_dist_C:
                    C = point
                    min_dist_C = dist
                elif point[0] < self.y[0] and point[1] > self.y[1] and dist < min_dist_D:
                    D = point
                    min_dist_D = dist
        
        return A, B, C, D
    



   
    