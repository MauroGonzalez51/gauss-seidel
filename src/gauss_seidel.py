import numpy as np


def gauss_seidel(coefficients: np.ndarray, independent_terms: np.ndarray, tolerance: float = 1e-6, max_iterations: int = 1000) -> np.ndarray:
    """
    Solves a system of linear equations using the Gauss-Seidel iterative method.

    Args:
        coefficients (np.ndarray): A square NumPy array representing the coefficient matrix of the system of linear equations.
        independent_terms (np.ndarray): A NumPy array representing the constant terms on the right-hand side of the equations (independent terms).
        tolerance (float, optional): The convergence tolerance for the solution. Defaults to 1e-6.
        max_iterations (int, optional): The maximum number of iterations allowed. Defaults to 1000.

    Returns:
        np.ndarray: A NumPy array containing the solution to the system of linear equations, or None if no solution is found within the maximum number of iterations.

    Raises:
        Exception: If no solution is found within the maximum number of iterations.
    """

    n = coefficients.shape[0]
    x = np.zeros(n)  # Initialize solution vector with zeros

    for _ in range(max_iterations):
        for j in range(n):
            # Temporary variable to store intermediate calculation
            d = independent_terms[j]

            # Iterate through all variables except the current one (j)
            for i in range(n):
                if i != j:
                    # Update temporary variable with weighted sum of previous solutions
                    d -= coefficients[j][i] * x[i]

            # Update the solution for the current variable (j)
            # Divide by diagonal element for new solution
            x[j] = d / coefficients[j][j]

        # Check convergence criteria (difference between solution and expected result)
        if np.max(np.abs(coefficients @ x - independent_terms)) < tolerance:
            return x

    raise Exception(
        "No solution found within the maximum number of iterations")


if __name__ == "__main__":
    pass  # Placeholder for main program logic (can be used for testing)
