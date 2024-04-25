import numpy as np

def gauss_seidel(coefficients: np.ndarray, independent_terms: np.ndarray, tolerance: float = 1e-6, max_iterations: int = 1000):
    n = coefficients.shape[0]
    x = np.zeros(n)

    for _ in range(max_iterations):
        for j in range(n):
            d = independent_terms[j]

            for i in range(n):
                if (j != i):
                    d -= coefficients[j][i] * x[i]

            x[j] = d / coefficients[j][j]

        if np.max(np.abs(coefficients @ x - independent_terms)) < tolerance:
            return x

if __name__ == "__main__":
    pass