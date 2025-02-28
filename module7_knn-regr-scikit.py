import numpy as np
from sklearn.neighbors import KNeighborsRegressor

class KNNRegressor:
    def __init__(self):
        """Initialize empty arrays for storing training data."""
        self.X_train = np.array([])
        self.y_train = np.array([])
        self.model = None

    def read_data(self, N):
        """Reads N (x, y) points from user input."""
        self.X_train = np.zeros((N, 1))  # Reshaped for scikit-learn compatibility
        self.y_train = np.zeros(N)
        print(f"Enter {N} (x, y) points:")
        for i in range(N):
            x = float(input(f"Enter x[{i+1}]: "))
            y = float(input(f"Enter y[{i+1}]: "))
            self.X_train[i] = x
            self.y_train[i] = y

    def compute_variance(self):
        """Computes and returns the variance of the y labels."""
        return np.var(self.y_train)

    def fit_model(self, k):
        """Fits the k-NN Regressor using scikit-learn."""
        if k > len(self.X_train):
            return None  # Error handling in predict function
        self.model = KNeighborsRegressor(n_neighbors=k, metric='euclidean')
        self.model.fit(self.X_train, self.y_train)

    def predict(self, X, k):
        """Performs k-NN Regression for input X using k neighbors."""
        if k > len(self.X_train):
            return "Error: k cannot be greater than N"
        self.fit_model(k)  # Ensure model is trained
        X_query = np.array([[X]])  # Reshape for scikit-learn
        return self.model.predict(X_query)[0]

def main():
    """Main function to run the k-NN Regression program."""
    # Step 1: Read N (number of points)
    N = int(input("Enter a positive integer N: "))

    # Step 2: Read k (number of neighbors)
    k = int(input("Enter a positive integer k: "))

    # Step 3: Read N data points
    regressor = KNNRegressor()
    regressor.read_data(N)

    # Step 4: Compute and print variance of Y labels
    variance = regressor.compute_variance()
    print("Variance of Y labels:", variance)

    # Step 5: Read X (query point)
    X = float(input("Enter X for prediction: "))

    # Step 6: Perform k-NN Regression and print result
    result = regressor.predict(X, k)
    print("Predicted Y:", result)

if __name__ == "__main__":
    main()
