import numpy as np

H = 0.0001


class FunVS:
    def __init__(self, f):
        self._f = f

    def __sub__(self, other):
        return FunVS(lambda x: self._f(x) - other._f(x))

    def __add__(self, other):
        return FunVS(lambda x: self._f(x) + other._f(x))

    def __mul__(self, scalar):
        return FunVS(lambda x: scalar * self._f(x))

    def __rmul__(self, scalar):
        return FunVS(lambda x: scalar * self._f(x))

    def __call__(self, x):
        return self._f(x)


def d(f, h=H):
    """first derivative"""

    def df(x):
        return np.imag(f(x + h * 1.0j)) / h

    return FunVS(df)


def d2(f, h=H):
    """second derivative"""

    def d2f(x):
        return (f(x - h) - 2.0 * f(x) + f(x + h)) / h**2.0

    return FunVS(d2f)


def integrate(f, x):
    return np.trapz(y=f(x), x=x)


def norm_h(g, tau_upper=30.0):
    """gives ||g||^2 for g : [0, inf) -> R"""
    dg = d(g)
    d2g = d2(g)
    d2g2 = FunVS(lambda x: d2g(x) ** 2.0)
    ntaus = int(tau_upper / 0.001)
    taus = np.linspace(0.0, tau_upper, ntaus)
    return (g(0) ** 2.0 + dg(0) ** 2.0 + integrate(d2g2, taus)) ** 0.5


def inner_polarization(a, b, norm):
    return (norm(a + b) ** 2 - norm(a - b) ** 2) / 4.0


def inner_h(a, b):
    return inner_polarization(a, b, norm_h)


def psi(tau, x):
    if not isinstance(x, np.ndarray):
        x = np.asarray([x])
    else:
        x = np.asarray(x)

    y = np.min([np.repeat(tau, len(x)), x], axis=0)

    return 1 - y**3 / 6 + tau * x * (2 + y) / 2


if __name__ == '__main__':
    psi_tau1 = FunVS(lambda x: psi(tau=1.0, x=x))
    g = FunVS(lambda x: np.exp(-1.0 * x))
    f = FunVS(lambda x: np.exp(-1.0 * x**2))

    for a in [g, f]:
        one = np.array([1.0])
        a1 = a(one)
        a1_from_inner = inner_h(psi_tau1, a)
        print(a1, a1_from_inner)
        print(a1 - a1_from_inner)
