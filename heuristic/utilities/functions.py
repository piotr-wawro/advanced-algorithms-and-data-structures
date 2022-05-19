import math

def rastrigin(X: list[float]) -> float:
    """
    Interval: <-10,10>
    Minimum: 0
    Solution: (0,...,0)
    """

    return 10*len(X) + sum(v**2 - 10*math.cos(2*math.pi*v) for v in X)

def rosenbrock(X: list[float]) -> float:
    """
    Interval: <-10,10>
    Minimum: 0
    Solution: (1,...,1)
    """

    value = 0
    for i in range(len(X)-1):
        value += 100 * ( X[i+1] - X[i]**2 )**2 + ( X[i] - 1 )**2

    return value

def hyper_ellipsoid(X: list[float]) -> float:
    """
    Interval: <-100,100>
    Minimum: 0
    Solution: (0,...,0)
    """

    value = 0
    for i in range(len(X)+1):
        for j in range(i):
            value += X[j]**2

    return value

def shubert(X: list[float]) -> float:
    """
    Interval: <-10,10>
    Minimum: -186.7
    Solution: (0,...,0)
    """

    return math.prod(sum(i*math.cos((i+1)*v) for i in range(1,6)) for v in X)

def sphere(X: list[float]) -> float:
    """
    Interval: <-10,10>
    Minimum: 0
    Solution: (0,...,0)
    """

    return sum(v**2 for v in X)

def sum_squares(X: list[float]) -> float:
    """
    Interval: <-10,10>
    Minimum: 0
    Solution: (0,...,0)
    """

    return sum(i*v**2 for i, v in enumerate(X))

def styblinski_tang(X: list[float]) -> float:
    """
    Interval: <-10,10>
    Minimum: -39.2n
    Solution: (-2.9,...,-2.9)
    """

    return 0.5*sum(v**4 - 16*v**2 + 5*v for v in X)

def weierstrass(X: list[float]) -> float:
    """
    Interval: <-30,30>
    Minimum: 0
    Solution: (-0.5,...,-0.5)
    """

    return sum((v + 0.5)**2 for v in X)
