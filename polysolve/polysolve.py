from __future__ import annotations
import numpy as np


CBRT_UNITY_IM = np.sqrt(3)/2 * 1j


def poly2(a: float,
          b: float,
          c: float) -> tuple[float, float]:
    """
    Solves the roots of a quadratic equation.

    Uses the quadratic formula. Result must be real.

    Parameters
    ----------
    a
       :math:`x^2` coefficient.
    b
       :math:`x` coefficient.
    c
       Constant value.

   Returns
   -------
   tuple[float, float]
       Positive and negative roots of quadratic.

   Examples
   --------
   >>> poly2(1., 0., 0.)
   (0.0, -0.0)
   >>> poly2(3., 0., -1.)
   (0.5773502691896257, -0.5773502691896257)Examples
   --------
   >>> poly2(1., 0., 0.)
   (0.0, -0.0)
   >>> quadratic(3., 0., -1.)
   (0.5773502691896257, -0.5773502691896257)
      
    """
    det = b**2 - (4*a*c)

    return ((-b + np.sqrt(det)) / (2*a),
            (-b - np.sqrt(det)) / (2*a))

def poly3(a: float,
          b: float,
          c: float,
          d: float) -> tuple[float, float, float]:
    """
    Solves the roots of a cubic equation.

    Uses the cubic formula. Result must be real.

    Parameters
    ----------
    a
       :math:`x^3` coefficient.
    b
       :math:`x^2` coefficient.
    c
       :math:`x` coefficient.
    d
       Constant value.

   Returns
   -------
   tuple[float, float, float]
       Positive and negative roots of quadratic.
    """
    q = (3*a*c - b**2) / (9*a**2)
    r = (9*a*b*c - 27*a**2*d - 2*b**3) / (54*a**3)

    s = np.cbrt(r + np.sqrt(q**3 + r**2))
    t = np.cbrt(r - np.sqrt(q**3 + r**2))

    x1 = s + t - (b/3*a)
    x2 = -(s + t)/2 - (b/3*a) + CBRT_UNITY_IM * (s - t)
    x3 = -(s + t)/2 - (b/3*a) - CBRT_UNITY_IM * (s - t)
    return x1, x2, x3

def poly(order: int,
         vec: tuple) -> tuple:
    if order < 2 or order > 3:
        raise Exception("I don't handle this polynome order")
    if order == 2:
        return poly2(*vec)
    if order == 3:
        return poly3(*vec)