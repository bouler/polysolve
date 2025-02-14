import pytest
import numpy as np
from polysolve.polysolve import poly2

def test_quadratic():
    params = [3., 0., -1.]
    roots = poly2(*params)
    assert all(np.isclose(np.polyval(params, root), 0.) for root in roots)
