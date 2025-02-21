import numpy as np

class KNNRegressor:
    def __init__(self):
        """Initialize empty arrays for storing training data."""
        self.X_train = np.array([])
        self.y_train = np.array([])

    def read_data(self, N):
        """Reads N (x, y) points from user input."""
        self.X_train = np.zeros(N)
        self.y_train = np.zeros(N)
        print(f"Enter {N} (x, y) points:")
        for i in range(N):
            x = float(input(f"Enter x[{i+1}]: "))
            y = float(input(f"Enter y[{i+1}]: "))
            self.X_train[i] = x
            self.y_train[i] = y

    def predict(self, X, k):
        """Performs k-NN Regression for input X using k neighbors."""
        N = len(self.X_train)
        if k > N:
            return "Error: k cannot be greater than N"

        # Compute Euclidean distances
        distances = np.abs(self.X_train - X)

        # Get indices of k nearest neighbors
        k_nearest_indices = np.argsort(distances)[:k]

        # Compute mean of corresponding y-values
        y_pred = np.mean(self.y_train[k_nearest_indices])
        return y_pred

def main():
    """Main function to run the k-NN Regression program."""
    # Step 1: Read N (number of points)
    N = int(input("Enter a positive integer N: "))

    # Step 2: Read k (number of neighbors)
    k = int(input("Enter a positive integer k: "))

    # Step 3: Read N data points
    regressor = KNNRegressor()
    regressor.read_data(N)

    # Step 4: Read X (query point)
    X = float(input("Enter X for prediction: "))

    # Step 5: Perform k-NN Regression and print result
    result = regressor.predict(X, k)
    print("Predicted Y:", result)

if __name__ == "__main__":
    main()
