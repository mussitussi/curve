import numpy as np
from utils import NUMBER, min_generic

H = 0.0001


class Fun:
    def __init__(self, f):
        self._f = f

    def __sub__(self, other):
        return Fun(lambda x: self(x) - other(x))

    def __add__(self, other):
        return Fun(lambda x: self(x) + other(x))
    
    def __mul__(self, other):
        if isinstance(other, NUMBER):
            return Fun(lambda x: other * self(x))
        elif callable(other):
            return Fun(lambda x: self(x) * other(x))
        else:
            raise ValueError(f'{other} must be a callable or a number')
        
    def __rmul__(self, other):
        return self * other

    @classmethod
    def zero(cls):
        return cls(lambda _: 0)

    def __call__(self, x):
        return self._f(x)


def d(f, h=H):
    """first derivative"""
    def df(x):
        return (f(x + h) - f(x)) / h

    return Fun(df)



def d2(f, h=H):
    """second derivative"""

    def d2f(x):
        return (f(x - h) - 2.0 * f(x) + f(x + h)) / h**2.0

    return Fun(d2f)


def integrate(f, a, b, h=H):
    x = np.arange(a, b + h, h)
    return np.trapz(f(x)) * h


def norm_h(g, tau_upper=30.0):
    """gives ||g|| for g : [0, inf) -> R"""
    dg = d(g)
    d2g = d2(g)
    d2g2 = Fun(lambda x: d2g(x) ** 2.0)
    return (g(0) ** 2.0 + dg(0) ** 2.0 + integrate(d2g2, 0, tau_upper)) ** 0.5


def inner_polarization(a, b, norm):
    """Theorem 4.1.4(iv) p.64 (polarization identity in a real vector space)"""
    return (norm(a + b) ** 2 - norm(a - b) ** 2) / 4.0


def inner_h(a, b):
    return inner_polarization(a, b, norm_h)


def psi(tau, x):
    y = min_generic(tau, x)
    return 1 - y**3 / 6 + tau * x * (2 + y) / 2


def _main():
    tau = 1.0
    psi_tau = Fun(lambda x: psi(tau=tau, x=x))
    exp = Fun(lambda x: np.exp(-1.0 * x))
    exp2 = Fun(lambda x: np.exp(-1.0 * x**2))
    
    
    for g in [exp, exp2]:
        g_at_tau = g(tau)
        g_at_tau_from_inner = inner_h(psi_tau, g)
        diff = g_at_tau - g_at_tau_from_inner
        print(f'tau={tau}:')
        print(f'g(tau)={g_at_tau}\t <psi_tau,g> = {g_at_tau_from_inner}')
        print(f'diff = {diff:.5e}')


if __name__ == '__main__':
    _main()
