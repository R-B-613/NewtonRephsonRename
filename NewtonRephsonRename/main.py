# This program about method of newton-rephson, with changes - for readability and code simplicity
# The function does not take into account the possibility of a root when p0=0
def newton_raphson(f, df, p0, tolerance=1e-6, max_iteration=50):
    p1 = None
    print("{:<10} {:<15} {:<15} ".format("Iteration", "po", "p1"))
    for i in range(max_iteration):
        if df(p0) == 0:
            print("Derivative is zero at p0, method cannot continue.")
            return                                         # Returns NONE if already at point p0 there is a 0 derivative

        p1 = p0 - f(p0) / df(p0)

        if abs(p1 - p0) < tolerance:                       # Check if the abs of p1-p0 not more than tolerance
            return p1                                      # Procedure completed successfully
        print("{:<10} {:<15.9f} {:<15.9f} ".format(i, p0, p1))
        p0 = p1
    return p1


if __name__ == '__main__':
    f = lambda x: x**3 - 3*x**2
    df = lambda x: 3*x**2 - 6*x
    p0 = -5                                                # Initial guess point
    tolerance = 1e-6
    max_iteration = 100
    roots = newton_raphson(f, df, p0, tolerance, max_iteration)
    # The root found after the iterations is returned to the newton_raphson function and entered into the roots variable
    print("\nThe equation f(x) has an approximate root at x = ", roots)

