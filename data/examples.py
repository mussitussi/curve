from collections import defaultdict
from dataclasses import dataclass
import numpy as np


@dataclass
class Bond:
    """simple annual coupon bond"""

    bond_id: int
    maturity: float
    coupon: float

    def __eq__(self, o):
        return isinstance(o, Bond) and self.bond_id == o.bond_id

    def __hash__(self):
        return hash(self.bond_id)


bond_data = {
    "bond_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "price": [96.60, 93.71, 91.56, 90.24, 89.74, 90.04, 91.09, 92.82, 95.19, 98.14],
    "maturity": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "coupon": [2.0, 2.5, 3.0, 3.5, 4, 4.5, 5.0, 5.5, 6.0, 6.5],
}

Payment = tuple[float, float]
Cashflow = list[Payment]
BondId = int

def bond2cf(b: Bond, face=100.0) -> Cashflow:
    coupon_payment = face * b.coupon / 100.0
    cf = []
    t = 1.0
    while t < b.maturity:
        cf.append((t, coupon_payment))
        t += 1

    cf.append((b.maturity, coupon_payment))
    cf.append((b.maturity, face))
    return cf


def cf_sum_by_date(cf: Cashflow) -> Cashflow:
    dct: defaultdict[float, float]
    dct = defaultdict(float)
    for p in cf:
        t, c = p
        dct[t] += c

    return list(sorted(dct.items()))


def cf_matrix(bonds: set[Bond]) -> dict[BondId, Cashflow]:
    cfs = []
    times = set()
    for b in bonds:
        cf = bond2cf(b)
        times.add(p[0] for p in cf)
        cfs.append(bond2cf(b))

    


if __name__ == "__main__":
    b = Bond(bond_id=1, maturity=1.0, coupon=5.0)
    cf = bond2cf(b)
    print(b)
    print(cf)
    print(cf_sum_by_date(cf))
